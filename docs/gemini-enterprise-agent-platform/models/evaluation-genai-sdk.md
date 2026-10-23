---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/evaluation-genai-sdk/
title: Tutorial: Perform evaluation using the GenAI Client in Agent Platform SDK \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:44:05.880450+00:00
---

# Tutorial: Perform evaluation using the GenAI Client in Agent Platform SDK  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/evaluation-genai-sdk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Tutorial: Perform evaluation using the GenAI Client in Agent Platform SDK Stay organized with collections  Save and categorize content based on your preferences. 

To see an example of Getting Started: Perform evaluation using the Agent Platform SDK through GenAI Client, run the "Getting Started: Perform evaluation using the Agent Platform SDK through GenAI Client" notebook in one of the following environments: 

[![](https://docs.cloud.google.com/static/vertex-ai/images/colab-logo-32px.png)Open in Colab](https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/gemini/evaluation/quick_start_gen_ai_eval.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/colab-enterprise-logo-32px.png)Open in Colab Enterprise](https://console.cloud.google.com/agent-platform/colab/import/https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fgenerative-ai%2Fmain%2Fgemini%2Fevaluation%2Fquick_start_gen_ai_eval.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/vertex-ai-workbench-logo-32px.png)Open in Agent Platform Workbench](https://console.cloud.google.com/agent-platform/workbench/deploy-notebook?download_url=https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fgenerative-ai%2Fmain%2Fgemini%2Fevaluation%2Fquick_start_gen_ai_eval.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/github-logo-32px.png)View on GitHub](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/evaluation/quick_start_gen_ai_eval.ipynb)

This page shows you how to evaluate your generative AI models and applications across a range of use cases using the GenAI Client in Agent Platform SDK.

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

  2. Install the Agent Platform SDK:
         
         !pip install google-cloud-aiplatform[evaluation]
         

  3. Set up your credentials. If you are running this tutorial in Colaboratory, run the following:
         
         from google.colab import auth
         auth.authenticate_user()
         

For other environments, refer to [Authenticate to Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/start/gcp-auth).




## Initialize the GenAI Client

To initialize the GenAI Client, run the following:
    
    
    from vertexai import Client
    
    client = Client(project="YOUR_PROJECT_ID", location="YOUR_LOCATION")
    

Where:

  * `YOUR_PROJECT_ID`: your Google Cloud project ID.
  * `YOUR_LOCATION`: your cloud region, for example, `us-central1`.



## Generate responses

Generate model responses for your dataset using `run_inference()`:

  1. [Prepare your dataset](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/evaluation-dataset) as a Pandas DataFrame:
         
         import pandas as pd
         
         eval_df = pd.DataFrame({
           "prompt": [
               "Explain software 'technical debt' using a concise analogy of planting a garden.",
               "Write a Python function to find the nth Fibonacci number using recursion with memoization, but without using any imports.",
               "Write a four-line poem about a lonely robot, where every line must be a question and the word 'and' cannot be used.",
               "A drawer has 10 red socks and 10 blue socks. In complete darkness, what is the minimum number of socks you must pull out to guarantee you have a matching pair?",
               "An AI discovers a cure for a major disease, but the cure is based on private data it analyzed without consent. Should the cure be released? Justify your answer."
           ]
         })
         

  2. Generate model responses using `run_inference()`:
         
         eval_dataset = client.evals.run_inference(
           model="gemini-2.5-flash",
           src=eval_df,
         )
         

  3. [Visualize your inference results](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/view-evaluation) by calling `.show()` on the `EvaluationDataset` object to inspect the model's outputs alongside your original prompts and references:
         
         eval_dataset.show()
         




The following image displays the evaluation dataset with prompts and their corresponding generated responses:

![A table showing an evaluation dataset with columns for prompts and responses.](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/models/images/evaluation-dataset.png)

## Run the evaluation

Run `evaluate()` to evaluate the model responses:

  1. Evaluate the model responses using the default `GENERAL_QUALITY` [adaptive rubric-based metric](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/determine-eval):
         
         eval_result = client.evals.evaluate(dataset=eval_dataset)
         

  2. [Visualize your evaluation results](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/view-evaluation) by calling `.show()` on the `EvaluationResult` object to display summary metrics and detailed results:
         
         eval_result.show()
         




The following image displays an evaluation report, which shows summary metrics and detailed results for each prompt-response pair.

![An evaluation report displaying summary metrics alongside detailed results for each prompt-response pair.](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/models/images/eval-report2.png)

## Clean up

No Gemini Enterprise Agent Platform resources are created during this tutorial.

## What's next

  * [Define your evaluation metrics](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/determine-eval).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
