---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-custom/
title: Hello custom training: Set up your project and environment \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:48.254562+00:00
---

# Hello custom training: Set up your project and environment  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-custom/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Hello custom training: Set up your project and environment Stay organized with collections  Save and categorize content based on your preferences. 

This page walks through setting up your Google Cloud project to use Gemini Enterprise Agent Platform and downloading some TensorFlow code for training. You will also download code for a web app that gets predictions.

This tutorial has several pages: 

  1. Setting up your project and environment. 

  2. [Training a custom image classification model.](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-custom/training)

  3. [Serving predictions from a custom image classification model.](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-custom/serving)

  4. [Cleaning up your project.](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-custom/cleanup)




Each page assumes that you have already performed the instructions from the previous pages of the tutorial.

## Before you begin

Throughout this tutorial, use Google Cloud console and [Cloud Shell](https://docs.cloud.google.com/shell/docs) to interact with Google Cloud. Alternatively, instead of Cloud Shell, you can use another Bash shell with the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs) installed.

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Gemini Enterprise Agent Platform and Cloud Run functions APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com,cloudfunctions)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Gemini Enterprise Agent Platform and Cloud Run functions APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com,cloudfunctions)

  8. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  9. If Cloud Shell does not display `(PROJECT_ID)$` in its prompt (where PROJECT_ID is replaced by your Google Cloud project ID), then run the following command to configure Cloud Shell to use your project:
         
         gcloud config set project PROJECT_ID
         




## Create a Cloud Storage bucket

Create a regional [Cloud Storage](https://docs.cloud.google.com/storage/docs) bucket in the `us-central1` region to use for the rest of this tutorial. As you follow the tutorial, use the bucket for several purposes:

  * Store training code for Agent Platform to use in a custom training job.
  * Store the model artifacts that your custom training job outputs.
  * Host the web app that gets predictions from your Agent Platform endpoint.



To create the Cloud Storage bucket, run the following command in your Cloud Shell session:
    
    
    gcloud storage buckets create gs://BUCKET_NAME --project=PROJECT_ID --location=us-central1
    

Replace the following:

  * PROJECT_ID: The ID of your Google Cloud project.
  * BUCKET_NAME: A name that you choose for your bucket. For example, `hello_custom_PROJECT_ID`. Learn about [requirements for bucket names](https://docs.cloud.google.com/storage/docs/buckets#naming).



## Download sample code

Download sample code to use for the rest of the tutorial.
    
    
    gcloud storage cp gs://cloud-samples-data/ai-platform/hello-custom/hello-custom-sample-v1.tar.gz - | tar -xzv
    

To optionally view the sample code files, run the following command:
    
    
    ls -lpR hello-custom-sample
    

The `hello-custom-sample` directory has four items:

  * `trainer/`: A directory of TensorFlow Keras code for training the flower classification model.

  * `setup.py`: A configuration file for packaging the `trainer/` directory into a Python source distribution that Agent Platform can use.

  * `function/`: A directory of Python code for a [Cloud Run function](https://docs.cloud.google.com/functions/docs) that can receive and preprocess prediction requests from a web browser, send them to Agent Platform, process the prediction responses, and send them back to the browser.

  * `webapp/`: A directory with code and markup for a web app that gets flower classification predictions from Agent Platform.




## What's next

Follow the [next page of this tutorial](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-custom/training) to run a custom training job on Agent Platform.

[ Previous arrow_back  Overview  ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-custom/overview)

[ Next Train a custom image classification model  arrow_forward  ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tutorials/image-classification-custom/training)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
