---
url: https://docs.cloud.google.com/dataform/docs/develop-with-ai/
title: Create actions with Gemini assistance \u00a0|\u00a0 Dataform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:44.674668+00:00
---

# Create actions with Gemini assistance  |  Dataform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/docs/develop-with-ai/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataform ](https://docs.cloud.google.com/dataform/docs)
  * [ Guides ](https://docs.cloud.google.com/dataform/docs/overview)



Send feedback 

#  Create actions with Gemini assistance Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — Gemini in Dataform**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can use [Gemini](https://docs.cloud.google.com/gemini/docs/overview), an AI-powered collaborator in Google Cloud, to generate SQL and Dataform core code inside `.sqlx` files in Dataform.

Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

Only English language prompts are supported for Gemini in Dataform. 

This document is intended for data analysts, data scientists, and data developers who work with [workflows in Dataform](https://docs.cloud.google.com/dataform/docs/sql-workflows). It assumes you have knowledge of Google SQL syntax and how to create Dataform workflow actions.

## Before you begin

  1. In the Google Cloud console, go to the project selector page.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
  3. [Activate Gemini in BigQuery](https://docs.cloud.google.com/gemini/docs/bigquery/set-up-gemini#activate).



## Generate a query

As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

You can provide Gemini with a natural language statement (or _prompt_) to generate a SQL or Dataform core query based on [workflow actions](https://docs.cloud.google.com/dataform/docs/sql-workflows) defined in your repository. For example, you can use Gemini to generate a SQL `SELECT` statement in a `.sqlx` table definition file.

To generate a SQL or Dataform core query, follow these steps:

  1. In the Google Cloud console, go to the **Dataform** page.

[Go to the Dataform page](https://console.cloud.google.com/bigquery/dataform)

  2. Select or [create a repository](https://docs.cloud.google.com/dataform/docs/create-repository), and then select or [create a workspace](https://docs.cloud.google.com/dataform/docs/create-workspace).

  3. In the **Files** pane, select or create a `.sqlx` file.

  4. In the file tab, click pen_spark **Gemini**.

  5. In the Gemini dialog, enter a natural language prompt.

If you know the SQL action that you want to use, then you can specify the action name in backticks (```) in your prompt.

  6. Click **Generate**.

Gemini reviews the SQL actions defined in your repository to find actions that might be relevant to your prompt and suggests a query.

  7. Optional: To provide feedback, click  thumb_up **Like suggestion** ,  thumb_down **Dislike suggestion** , or  chat_info **Give more feedback**

  8. To accept the suggestion, click **Insert**.




### Tips for query generation

The following tips can improve suggestions that Gemini in Dataform provides:

  * Provide the SQL action name enclosed in backticks (```), such as ````action_name````.
  * If the column names or their semantic relationships are unclear or complex, then you can provide context in the prompt to guide Gemini towards the answer that you want. This technique is known as _prompt engineering_. For example, to encourage a generated query to reference a column name, describe the column name and its relevance to the answer that you want. To encourage an answer that references complex terms like _lifetime value_ or _gross margin_ , describe the concept and its relevance to your data to improve SQL generation results.



### Gemini and Dataform data

Gemini in Dataform can access the metadata of the tables that you have permission to access. This can include the table names, column names, data types, and column descriptions. Gemini in Dataform cannot access the data in your tables, views, or models. For more information on how Gemini uses your data, see [How Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

## What's next

  * For information about Gemini for Google Cloud, see [Gemini for Google Cloud overview](https://docs.cloud.google.com/gemini/docs/overview).
  * For information about the Gemini data policy, see [How Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
