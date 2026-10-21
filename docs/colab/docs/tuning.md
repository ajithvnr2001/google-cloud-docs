---
url: https://docs.cloud.google.com/colab/docs/tuning/
title: Tune a model \u00a0|\u00a0 Colab Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:30:20.564301+00:00
---

# Tune a model  |  Colab Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/colab/docs/tuning/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Colab Enterprise ](https://docs.cloud.google.com/colab/docs)
  * [ Guides ](https://docs.cloud.google.com/colab/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Tune a model

This page shows you how to interact with Gemini Enterprise Agent Platform to tune a model by using the side panel in Colab Enterprise.

To access Google Cloud services and APIs by running code in your Colab Enterprise notebook, you can use the credentials associated with your Google Account. To learn more, see [Access Google Cloud services and APIs](https://docs.cloud.google.com/colab/docs/run-code-adc).

The side panel is an additional way to interact with Agent Platform to tune models without leaving the Colab Enterprise interface.

The side panel appears to the right of an open notebook.

## Model tuning in Agent Platform

_Model tuning_ is an effective way to customize large models to your tasks. It's a key step to improving the model's quality and efficiency. Model tuning provides the following benefits:

  * Higher quality for your specific tasks
  * Increased model robustness
  * Lower inference latency and cost due to shorter prompts



For an overview of Agent Platform model tuning for Gemini, see [Introduction to tuning](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Agent Platform, Dataform, and Compute Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com,dataform.googleapis.com,compute.googleapis.com&redirect=https%3A//console.cloud.google.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Agent Platform, Dataform, and Compute Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com,dataform.googleapis.com,compute.googleapis.com&redirect=https%3A//console.cloud.google.com)




### Required roles

To get the permissions that you need to use the side panel in a Colab Enterprise notebook, ask your administrator to grant you the following IAM roles on the project: 

  * [Colab Enterprise User ](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.colabEnterpriseUser) (`roles/aiplatform.colabEnterpriseUser`)
  * [Agent Platform User ](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.user) (`roles/aiplatform.user`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

One or more of the required roles includes the `dataform.repositories.list` permission. Users who are granted the `dataform.repositories.list` permission or the [Code Creator (`roles/dataform.codeCreator`)](https://docs.cloud.google.com/dataform/docs/access-control#dataform.codeCreator) role in a project can list the names of code assets in that project by using the Dataform API or the Dataform command-line interface (CLI). Non-administrators using BigQuery Studio can only see code assets that they created or that were shared with them. 

## Tune a model

You can tune a model in Agent Platform by using the side panel in Colab Enterprise. 

  1. In the Google Cloud console, go to the Colab Enterprise **My notebooks** page. 

[Go to My notebooks](https://console.cloud.google.com/agent-platform/colab/notebooks)

  2. In the **Region** menu, select the region that contains your notebook.

  3. Click the notebook that you want to open. If you haven't created a notebook yet, [create a notebook](https://docs.cloud.google.com/colab/docs/create-console-quickstart#create). 

  4. To the right of your notebook, in the side panel, click the ![](https://docs.cloud.google.com/static/colab/images/icon-tuning.png) **Tuning** button. 

The side panel expands the **Tuning** tab.

  5. Click the **Tune a Gemini model** button.

Colab Enterprise adds code cells to your notebook for tuning a Gemini model. 

  6. In your notebook, find the code cell that stores parameter values. You'll use these parameters to interact with Agent Platform. 

  7. Update the values for the following parameters:

     * `PROJECT_ID`: The ID of the project that your notebook is in. 
     * `REGION`: The region that your notebook is in. 
     * `TUNED_MODEL_DISPLAY_NAME`: The name of your tuned model. 
  8. In the next code cell, update the model tuning parameters:

     * `source_model`: The Gemini model that you want to use, for example, `gemini-2.0-flash-001`. 
     * `train_dataset`: The URL of your training dataset. 
     * `validation_dataset`: The URL of your validation dataset. 
     * Adjust the remaining parameters as needed. 
  9. Run the code cells that the side panel added to your notebook.

  10. After the last code cell runs, click the ![](https://docs.cloud.google.com/static/colab/images/icon-tuning.png) **View tuning job** button that appears. 

  11. The side panel shows information about your model tuning job.

     * The **Monitor** tab shows tuning metrics when the metrics are ready. 
     * The **Dataset** tab shows a summary and metrics about your dataset after the dataset has been processed. 
     * The **Details** tab shows information about your tuning job, such as the tuning method and the base model (source model) that you used. 
  12. After the tuning job has completed, you can go directly from the **Tuning details** tab to a page where you can test your model. Click **Test**. 

The Google Cloud console opens to the Agent Platform **Text chat** page, where you can test your model. 




## View details of a tuning job

You can view the details of a tuning job, even if you didn't create and run the tuning job in Colab Enterprise. You can view a tuning job's details by using the side panel in Colab Enterprise.

  1. In the Google Cloud console, go to the Colab Enterprise **My notebooks** page. 

[Go to My notebooks](https://console.cloud.google.com/agent-platform/colab/notebooks)

  2. In the **Region** menu, select the region that contains your notebook.

  3. Click the notebook that you want to open. If you haven't created a notebook yet, [create a notebook](https://docs.cloud.google.com/colab/docs/create-console-quickstart#create). 

  4. To the right of your notebook, in the side panel, click the ![](https://docs.cloud.google.com/static/colab/images/icon-tuning.png) **Tuning** button. 

The side panel expands the **Tuning** tab.

  5. Click the **View tuning job details** button.

Colab Enterprise adds code cells to your notebook for getting the details of a tuning job. 

  6. In your notebook, find the code cell that stores parameter values. You'll use these parameters to interact with Agent Platform. 

  7. Update the values for the following parameters:

     * `PROJECT_ID`: The ID of the project that your notebook is in. 
     * `REGION`: The region that your notebook is in. 
     * `TUNING_JOB_ID`: The ID of your Agent Platform tuning job. 
  8. Run the code cells that the side panel added to your notebook.

  9. After the last code cell runs, click the ![](https://docs.cloud.google.com/static/colab/images/icon-tuning.png) **View tuning job** button that appears. 

  10. The side panel shows information about your model tuning job.

     * The **Monitor** tab shows tuning metrics when the metrics are ready. 
     * The **Dataset** tab shows a summary and metrics about your dataset after the dataset has been processed. 
     * The **Details** tab shows information about your tuning job, such as the tuning method and the base model (source model) that you used. 



## What's next

  * Learn more about [model tuning in Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning).

  * To learn more about model tuning parameters, see [Tune Gemini models by using supervised fine-tuning](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning/supervised-tuning/use).

  * To find a notebook that can help you get your project started quickly, see the [notebook gallery](https://console.cloud.google.com/agent-platform/colab/notebook-gallery). 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
