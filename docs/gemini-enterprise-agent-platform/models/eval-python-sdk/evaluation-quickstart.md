---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/eval-python-sdk/evaluation-quickstart/
title: Tutorial: Perform evaluation using the Python SDK \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:44:14.765840+00:00
---

# Tutorial: Perform evaluation using the Python SDK  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/eval-python-sdk/evaluation-quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Tutorial: Perform evaluation using the Python SDK

To see an example of Getting started with the Agent Platform Python SDK for Gen AI evaluation service, run the "Getting Started with the Agent Platform Python SDK for Gen AI evaluation service" notebook in one of the following environments: 

[![](https://docs.cloud.google.com/static/vertex-ai/images/colab-logo-32px.png)Open in Colab](https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/gemini/evaluation/evaltask_approach/intro_to_gen_ai_evaluation_service_sdk.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/colab-enterprise-logo-32px.png)Open in Colab Enterprise](https://console.cloud.google.com/agent-platform/colab/import/https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fgenerative-ai%2Fmain%2Fgemini%2Fevaluation%2Fevaltask_approach%2Fintro_to_gen_ai_evaluation_service_sdk.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/vertex-ai-workbench-logo-32px.png)Open in Agent Platform Workbench](https://console.cloud.google.com/agent-platform/workbench/deploy-notebook?download_url=https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fgenerative-ai%2Fmain%2Fgemini%2Fevaluation%2Fevaltask_approach%2Fintro_to_gen_ai_evaluation_service_sdk.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/github-logo-32px.png)View on GitHub](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/evaluation/evaltask_approach/intro_to_gen_ai_evaluation_service_sdk.ipynb)

This page shows you how to perform a model-based evaluation with Gen AI evaluation service using the Agent Platform SDK for Python.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

[Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

[Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  2. Install the Agent Platform SDK for Python with Gen AI evaluation service dependency:
         
         !pip install google-cloud-aiplatform[evaluation]
         

  3. Set up your credentials. If you are running this quickstart in Colaboratory, run the following:
         
         from google.colab import auth
         auth.authenticate_user()
         

For other environments, refer to [Authenticate to Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/authentication#client-libraries). 




## Import libraries

Import your libraries and set up your project and location.
    
    
    import pandas as pd
    
    import [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest)
    from vertexai.evaluation import EvalTask, PointwiseMetric, PointwiseMetricPromptTemplate
    from google.cloud import aiplatform
    
    PROJECT_ID = "PROJECT_ID"
    LOCATION = "LOCATION"
    EXPERIMENT_NAME = "EXPERIMENT_NAME"
    
    [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest).[init](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.html)(
        project=PROJECT_ID,
        location=LOCATION,
    )

Note that `EXPERIMENT_NAME` can only contain lowercase alphanumeric characters and hyphens, up to a maximum of 127 characters.

## Set up evaluation metrics based on your criteria

The following metric definition evaluates the text quality generated from a large language model based on two criteria: `Fluency` and `Entertaining`. The code defines a metric called `custom_text_quality` using those two criteria:
    
    
    custom_text_quality = PointwiseMetric(
        metric="custom_text_quality",
        metric_prompt_template=PointwiseMetricPromptTemplate(
            criteria={
                "fluency": (
                    "Sentences flow smoothly and are easy to read, avoiding awkward"
                    " phrasing or run-on sentences. Ideas and sentences connect"
                    " logically, using transitions effectively where needed."
                ),
                "entertaining": (
                    "Short, amusing text that incorporates emojis, exclamations and"
                    " questions to convey quick and spontaneous communication and"
                    " diversion."
                ),
            },
            rating_rubric={
                "1": "The response performs well on both criteria.",
                "0": "The response is somewhat aligned with both criteria",
                "-1": "The response falls short on both criteria",
            },
        ),
    )
    

## Prepare your dataset

Add the following code to prepare your dataset:
    
    
    responses = [
        # An example of good custom_text_quality
        "Life is a rollercoaster, full of ups and downs, but it's the thrill that keeps us coming back for more!",
        # An example of medium custom_text_quality
        "The weather is nice today, not too hot, not too cold.",
        # An example of poor custom_text_quality
        "The weather is, you know, whatever.",
    ]
    
    eval_dataset = pd.DataFrame({
        "response" : responses,
    })
    

## Run evaluation with your dataset

Run the evaluation:
    
    
    eval_task = EvalTask(
        dataset=eval_dataset,
        metrics=[custom_text_quality],
        experiment=EXPERIMENT_NAME
    )
    
    pointwise_result = eval_task.evaluate()
    
    

View the evaluation results for each response in the `metrics_table` Pandas DataFrame:
    
    
    pointwise_result.metrics_table
    

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

Delete the `ExperimentRun` created by the evaluation:
    
    
    aiplatform.ExperimentRun(
        run_name=pointwise_result.metadata["experiment_run"],
        experiment=pointwise_result.metadata["experiment"],
    ).delete()
    
    

## What's next

  * [Define your evaluation metrics](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/eval-python-sdk/determine-eval).

  * [Prepare your evaluation dataset](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/eval-python-sdk/evaluation-dataset).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
