---
url: https://docs.cloud.google.com/colab/docs/use-code-completion/
title: Use code completion and code generation \u00a0|\u00a0 Colab Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:19:26.533123+00:00
---

# Use code completion and code generation  |  Colab Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/colab/docs/use-code-completion/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Colab Enterprise ](https://docs.cloud.google.com/colab/docs)
  * [ Guides ](https://docs.cloud.google.com/colab/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use code completion and code generation

This document describes how you can use Gemini in Colab Enterprise, which is a product in the [Gemini for Google Cloud](https://docs.cloud.google.com/gemini/docs/overview) portfolio, to help you write and generate code in a Colab Enterprise notebook.

Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

This document is intended for data analysts, data scientists, and data developers who work with Colab Enterprise. It assumes you have knowledge of how to write code in a notebook environment.

## Limitations

[Colab](https://colab.research.google.com)'s Transform Code feature isn't supported in Colab Enterprise. To learn about other ways to use AI-powered features to help you edit code in Colab Enterprise, see [Use the Data Science Agent](https://docs.cloud.google.com/colab/docs/use-data-science-agent).

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

## Enable code completion and code generation

To enable code completion and code generation, do the following:

  1. In the Google Cloud console, go to the Colab Enterprise **My notebooks** page. 

[Go to My notebooks](https://console.cloud.google.com/agent-platform/colab/notebooks)

  2. In the toolbar, click the pen_spark **Help me code** button and select the features that you want to use. 

![The list of Gemini in Colab Enterprise features under the Help me code button, including code completion and code generation.](https://docs.cloud.google.com/static/colab/images/ai-code-features.png)
     * **Code completion** suggests code while you type.
     * **Code generation** generates code from a description of what you want. 

If the pen_spark **Help me code** button isn't active, or if you don't see a list of features when you click the button, see [Set up Gemini in Colab Enterprise for a project](https://docs.cloud.google.com/colab/docs/gemini-in-colab/set-up-gemini). 




## Use code completion

To use code completion in a Colab Enterprise notebook, do the following: 

  1. In the Google Cloud console, go to the Colab Enterprise **My notebooks** page. 

[Go to My notebooks](https://console.cloud.google.com/agent-platform/colab/notebooks)

  2. In the **Region** menu, select the region that contains your notebook.

  3. Click the notebook that you want to open.

  4. In the toolbar, click the pen_spark **Help me code** button and select **Code completion** if it isn't already selected. 
  5. In a code cell of your notebook, start entering code. Colab Enterprise suggests a potential way to complete your code in gray italic text. 

For example, if you enter `import p`, Colab Enterprise might suggest a code completion that imports `pandas as pd` followed by a line that reads a CSV file and stores the contents in a pandas dataframe.  
![](https://docs.cloud.google.com/static/colab/images/code-completion.png)

  6. To accept the suggested code completion, press `Tab`.




## Use code generation

To generate code using Gemini for Google Cloud:

  1. In the Google Cloud console, go to the Colab Enterprise **My notebooks** page. 

[Go to My notebooks](https://console.cloud.google.com/agent-platform/colab/notebooks)

  2. In the **Region** menu, select the region that contains your notebook.

  3. Click the notebook that you want to open.

  4. In the toolbar, click the pen_spark **Help me code** button and select **Code generation** if it isn't already selected. 

  5. In your notebook, add a blank code cell, or click a code cell that doesn't have any code in it. 

  6. Click pen_spark **Available AI features** , and then click **Generate code**. 

  7. In the pen_spark **Generate** field, type a description of the code that you want to generate, and then press `Enter`. 

  8. To close the **Generate** panel, click **Close**. 




## Turn off code completion and code generation

To turn off code completion and code generation, do the following:

  1. In the Colab Enterprise toolbar, click the pen_spark **Help me code** button.

  2. Clear the features that you want to turn off.




## Troubleshoot

This section shows you how to resolve issues with using Gemini in Colab Enterprise.

### Gemini features not working

When you type in a Colab Enterprise notebook, code completion suggestions don't appear. Or, the pen_spark **Help me code** button doesn't appear above a code cell. 

In your Colab Enterprise settings, you might have turned off the **Show context-powered code completions** setting. 

To resolve this issue, do the following: 

  1. Click arrow_drop_down **Toggle header visibility**. 
  2. On the **Tools** menu, click **Settings**.
  3. Click **Editor**.
  4. Select **Show context-powered code completions**.
  5. Click **Save**.



## What's next

  * Read the [Gemini for Google Cloud overview](https://docs.cloud.google.com/gemini/docs/overview).

  * For more ways to write and edit code with Gemini assistance, see the following:

    * [Chat about your notebook with Gemini](https://docs.cloud.google.com/colab/docs/chat)
    * [Explain code cells](https://docs.cloud.google.com/colab/docs/explain-cells)
    * [Explain and fix errors](https://docs.cloud.google.com/colab/docs/explain-errors)
    * [Use the Data Science Agent](https://docs.cloud.google.com/colab/docs/use-data-science-agent)
  * Learn [how Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
