---
url: https://docs.cloud.google.com/colab/docs/explain-errors/
title: Explain and fix errors with Gemini assistance \u00a0|\u00a0 Colab Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:48.372225+00:00
---

# Explain and fix errors with Gemini assistance  |  Colab Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/colab/docs/explain-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Colab Enterprise ](https://docs.cloud.google.com/colab/docs)
  * [ Guides ](https://docs.cloud.google.com/colab/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Explain and fix errors with Gemini assistance

This document describes how you can use Gemini in Colab Enterprise, which is a product in the [Gemini for Google Cloud](https://docs.cloud.google.com/gemini/docs/overview) portfolio, to help you explain and fix errors in a Colab Enterprise notebook.

Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

This document is intended for data analysts, data scientists, and data developers who work with Colab Enterprise. It assumes you have knowledge of how to write code in a notebook environment.

## Overview

When you run code that generates an error, Gemini in Colab Enterprise can suggest a fix or explain the error to help you resolve the issue.

## Before you begin

As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

  1. [Ensure that Gemini in Colab Enterprise is set up for your Google Cloud user account and project. ](https://docs.cloud.google.com/gemini/docs/colab/set-up-gemini)

  2. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  3. Enable the Agent Platform, Gemini for Google Cloud, Dataform, and Compute Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com,cloudaicompanion.googleapis.com,dataform.googleapis.com,compute.googleapis.com)

  4. Enable the Agent Platform, Gemini for Google Cloud, Dataform, and Compute Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com,cloudaicompanion.googleapis.com,dataform.googleapis.com,compute.googleapis.com)




### Required roles

To get the permissions that you need to use Gemini in Colab Enterprise, ask your administrator to grant you the following IAM roles on the project: 

  * [Colab Enterprise User ](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.colabEnterpriseUser) (`roles/aiplatform.colabEnterpriseUser`)
  * [Gemini for Google Cloud User ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudaicompanion#cloudaicompanion.user) (`roles/cloudaicompanion.user`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

One or more of the required roles includes the `dataform.repositories.list` permission. Users who are granted the `dataform.repositories.list` permission or the [Code Creator (`roles/dataform.codeCreator`)](https://docs.cloud.google.com/dataform/docs/access-control#dataform.codeCreator) role in a project can list the names of code assets in that project by using the Dataform API or the Dataform command-line interface (CLI). Non-administrators using BigQuery Studio can only see code assets that they created or that were shared with them. 

## Explain and fix an error

To use Gemini for Google Cloud to explain and fix an error in your code, do the following:

  1. In the Google Cloud console, go to the Colab Enterprise **My notebooks** page. 

[Go to My notebooks](https://console.cloud.google.com/agent-platform/colab/notebooks)

  2. In the **Region** menu, select the region that contains your notebook.

  3. Click the notebook that you want to open.

  4. In a code cell of your notebook, enter code that contains an error, and then run the cell. For example, you might enter `print(a + random())` without defining `a`. 

After your code cell runs, Colab Enterprise prints an error message below your code cell. If Gemini in Colab Enterprise has an explanation for this error, an **Explain error** button appears. 

  5. Click the **Explain error** button.

If you haven't already authorized the Data Science Agent, a brief dialog appears while Colab Enterprise authenticates your Google Account to the Data Science Agent. 

  6. Colab Enterprise opens a chat dialog that contains an explanation of the error. The dialog might also include recommendations and suggested changes for how to resolve the problem. 

After evaluating the content, you can do any of the following:

     * If Gemini provides a suggested code edit in its response, you can click: 
       * **Accept** to update the code in your notebook.
       * **Accept and run** to update and run the code.
       * **Cancel** to reject the edit.
     * Use the chat dialog to discuss the error with Gemini. 
  7. To close the chat dialog, click close **Close**. 




## Turn off Gemini in Colab Enterprise

To turn off Gemini in Colab Enterprise for a Google Cloud project, an administrator must turn off the Gemini for Google Cloud API. See [Disabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable#disabling). 

To turn off Gemini in Colab Enterprise for a specific user, an administrator needs to revoke the [Gemini for Google Cloud User](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudaicompanion#cloudaicompanion.user) (`roles/cloudaicompanion.user`) role for that user. See [Revoke a single IAM role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#revoke-single-role). 

## What's next

  * Read the [Gemini for Google Cloud overview](https://docs.cloud.google.com/gemini/docs/overview).

  * For more ways to write and edit code with Gemini assistance, see the following:

    * [Chat about your notebook with Gemini](https://docs.cloud.google.com/colab/docs/chat)
    * [Use code completion and code generation](https://docs.cloud.google.com/colab/docs/use-code-completion)
    * [Explain code cells](https://docs.cloud.google.com/colab/docs/explain-cells)
    * [Use the Data Science Agent](https://docs.cloud.google.com/colab/docs/use-data-science-agent)
  * Learn [how Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
