---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/before-you-begin/
title: Before you begin \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:35:17.203939+00:00
---

# Before you begin  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/before-you-begin/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Before you begin Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the basic start-up tasks that you must complete before using Agent Search.

## Create a project

To create a Google Cloud project for your Agent Search apps and data stores, follow these steps:

  1. In the Google Cloud console, on the [project selector page](https://console.cloud.google.com/projectselector2/home/dashboard), select or [create a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

  2. Make sure that billing is enabled for your Google Cloud project. Learn how to [check if billing is enabled on a project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled).

  3. If you plan to use the API, [install](https://docs.cloud.google.com/sdk/docs/install) and [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI.




## Turn on Agent Search

To use Agent Search, you must activate the Agent Search service.

To turn on Agent Search, follow these steps:

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/start)

  2. Optional: Click **Allow Google to selectively sample model input and responses**.

  3. Optional: Review the [terms for data use](https://cloud.google.com/retail/data-use-terms).

  4. Click **Continue and activate the API**.




## Access control in Agent Search

You can configure access control for Agent Search at the project level. To grant access to Agent Search using the console, grant the Discovery Engine Admin role to a principal for the project that contains the Agent Search engine.

To grant access to Agent Search, follow the instructions at [Grant a single role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#iam-grant-single-role-console) in the IAM documentation using the following guidance:

  * Select the project that contains the Agent Search engine.

  * When selecting a role, enter **Discovery Engine** in the filter, and then click **Discovery Engine Admin**.




If you are an owner of the project, you automatically have the Discovery Engine Admin role for that project.

To grant access to Agent Search for other users, groups, and service accounts, see [Access control with IAM](https://docs.cloud.google.com/generative-ai-app-builder/docs/access-control).

If you are using the API, see [Set up authentication on Google Cloud](https://docs.cloud.google.com/generative-ai-app-builder/docs/authentication#on-gcp) for authentication and access control.

## What's next

  * [Authenticate to Agent Search](https://docs.cloud.google.com/generative-ai-app-builder/docs/authentication)
  * [Access control with IAM](https://docs.cloud.google.com/generative-ai-app-builder/docs/access-control)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
