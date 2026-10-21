---
url: https://docs.cloud.google.com/colab/docs/gemini-in-colab/set-up-gemini/
title: Set up Gemini in Colab Enterprise for a project \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:52:30.852590+00:00
---

# Set up Gemini in Colab Enterprise for a project  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/colab/docs/gemini-in-colab/set-up-gemini/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Colab Enterprise ](https://docs.cloud.google.com/colab/docs)
  * [ Guides ](https://docs.cloud.google.com/colab/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up Gemini in Colab Enterprise for a project

Before you can use [Gemini in Colab Enterprise](https://docs.cloud.google.com/colab/docs/gemini-in-colab/overview), your team needs to activate Gemini in Colab Enterprise in a Google Cloud project, as described in this document. An administrator typically performs this step.

## Activate Gemini in Colab Enterprise in a Google Cloud project

To activate Gemini in Colab Enterprise in a Google Cloud project, an administrator needs to enable the Gemini for Google Cloud API and grant the Gemini for Google Cloud User role to users.

  1. To enable the Gemini for Google Cloud API, in the Google Cloud console, go to the **Gemini for Google Cloud** page.

[Go to Gemini for Google Cloud](https://console.cloud.google.com/marketplace/product/google/cloudaicompanion.googleapis.com)

  2. In the project selector, select a project.

  3. Click **Enable**.

The page updates and shows a status of **Enabled**. Gemini is now available in the selected Google Cloud project to all users who have the required IAM roles.

  4. To grant the IAM roles that are required to use Gemini, go to the **IAM & Admin** page.

[Go to IAM & Admin](https://console.cloud.google.com/projectselector/iam-admin/iam)

  5. In the **Principal** column, find a [principal](https://docs.cloud.google.com/iam/docs/overview#concepts_related_identity) for which you want to give access to Gemini in Colab Enterprise, and then click edit **Edit principal** in that row.

  6. In the **Edit access** pane, click add **Add another role**.

  7. In **Select a role** , select **Gemini for Google Cloud User**.

  8. Click **Save**.




All of the users who have been granted these roles can access Gemini features in the Google Cloud console within the specified project. For more information, see [Gemini for Google Cloud overview](https://docs.cloud.google.com/gemini/docs/overview).

## Advanced setup tasks

Instead of using the Google Cloud console or the gcloud CLI to grant predefined IAM roles, you can do any of the following:

  * Use [IAM REST APIs](https://docs.cloud.google.com/iam/docs/reference/rest) or [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries) to grant roles.

If you use these interfaces, use the fully qualified role name, `roles/cloudaicompanion.user`.

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

  * Create and grant custom roles.

Any [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) that you create need the following permissions to access Gemini:

    * `cloudaicompanion.instances.generateCode`
    * `cloudaicompanion.instances.completeCode`
    * `cloudaicompanion.entitlements.get`



## Billing

Gemini in Colab Enterprise is currently available to try at no additional cost. See [Colab Enterprise pricing](https://cloud.google.com/colab/pricing).

## What's next

  * Learn how to [write code with Gemini assistance](https://docs.cloud.google.com/colab/docs/use-code-completion).
  * Learn more about the [types of generative AI assistance available in Gemini for Google Cloud](https://docs.cloud.google.com/gemini/docs/overview).
  * Learn [how Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).
  * Learn [how to access and manage Gemini admin controls](https://docs.cloud.google.com/gemini/docs/admin).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
