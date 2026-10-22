---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/evaluation-genai-console/
title: Tutorial: Perform evaluation using the console \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:40:57.080648+00:00
---

# Tutorial: Perform evaluation using the console  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/evaluation-genai-console/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Tutorial: Perform evaluation using the console Stay organized with collections  Save and categorize content based on your preferences. 

Learn how to get started with Gen AI evaluation service using the Google Google Cloud console.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Make sure that you have the following role or roles on the project: Storage Admin 

#### Check for the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

     4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 

#### Grant the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. Click person_add **Grant access**. 
     4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

     5. Click **Select a role** , then search for the role. 
     6. To grant additional roles, click add **Add another role** and add each additional role. 
     7. Click **Save**. 

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Make sure that you have the following role or roles on the project: Storage Admin 

#### Check for the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

     4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 

#### Grant the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. Click person_add **Grant access**. 
     4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

     5. Click **Select a role** , then search for the role. 
     6. To grant additional roles, click add **Add another role** and add each additional role. 
     7. Click **Save**. 




## Evaluate your model

To evaluate your model:

  1. In the Google Cloud console, go to the Gen AI Evaluation page.

[Go to Evaluation](https://console.cloud.google.com/agent-platform/evaluation)

  2. Click **New evaluation** to open the evaluation page.

  3. Select a source to load a dataset for evaluation:

     * To upload a local CSV or JSONL file, select **Upload file**. The dataset must contain either prompts or records to use in a prompt template and, optionally, model responses. The maximum is 200 rows.

     * To generate prompts from a prompt template, select **Generate data**. The Gen AI evaluation service generates and populates the variables that you defined in your prompt template when creating your dataset. For more information about authoring prompt templates, see [Use prompt templates](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/prompts/prompt-templates).

       1. Enter your prompt template with your variables in the **Prompt template** field.

       2. To add a description for each of your variables or to specify the number of samples to generate, expand **Define variables and sample size**.

       3. Click **Generate dataset** to generate prompts.

  4. Generate and evaluate responses based on your prompts:

     1. In the **Evaluation candidates** section, click **Add evaluation candidate** , or if a candidate already exists, click edit **Edit** to define the prompts and responses to evaluate. For example, you can specify prompts or responses from your uploaded file or from generated data.

     2. To compare multiple candidates, click **Add comparison candidate**.

     3. In the **Metrics** section, add at least one metric to score the quality of your candidate's responses. For more information about the metric types, see the [Evaluation metrics](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/evaluation-overview#metrics) section on the Gen AI evaluation service overview page.

For some adaptive rubrics, you can steer the rubrics that are generated from each prompt by expanding **Advanced** and providing custom instructions, such as `Evaluate the dataset on cultural sensitivity`.

     1. In the **Name and storage configuration** section, specify a name for your evaluation and a Cloud Storage bucket where your evaluations results are stored.
  5. Click **Evaluate**.




## View your evaluation results

To view an evaluation result:

  1. In the Google Cloud console, go to the **GenAI Evaluation** page.

[Go to Evaluation](https://console.cloud.google.com/agent-platform/evaluation)

  2. Click the evaluation name.

For each prompt in your evaluation dataset, the response is shown along with the evaluation results.




## Evaluate partner models

You can use Gen AI evaluation service to evaluate the following partner models:

  * **Anthropic**
  * **Llama**



Partner models are supported through Gemini Enterprise Agent Platform Model Garden. You must enable a partner model in [Model Garden](https://console.cloud.google.com/agent-platform/model-garden) before selecting it for evaluation. To evaluate a partner model, select it in the model selection menu during evaluation setup.

### Pricing

Pricing for evaluating third-party models is based on any charges incurred for model inference in Gemini Enterprise Agent Platform Model Garden. See the [Pricing page for Generative AI on Agent Platform](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing).

## What's next

  * [Define your evaluation metrics](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/determine-eval).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
