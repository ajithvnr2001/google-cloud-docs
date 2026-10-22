---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/before-you-begin/
title: Quickstart: Enable Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:36:27.212929+00:00
---

# Quickstart: Enable Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/before-you-begin/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Enable Customer Experience Insights

Before using Customer Experience Insights (CX Insights) to analyze conversational data, you must enable specific APIs.

In this quickstart, you will complete the following actions:

  1. Enable the APIs:

     * **Cloud Speech-to-Text API** —to upload audio files.
     * **Cloud Storage API** —to ingest conversations into CX Insights.
     * **Contact Center AI Insights API** —to use CX Insights.
     * **Dialogflow API** —to support [Dialogflow runtime integration](https://docs.cloud.google.com/gemini-enterprise-cx/insights/dialogflow-runtime-integration) and [topic modeling](https://docs.cloud.google.com/gemini-enterprise-cx/insights/topic-modeling-overview).
     * **Sensitive Data Protection (DLP) API** —to perform [redaction on audio or transcript files](https://docs.cloud.google.com/gemini-enterprise-cx/insights/ingest-conversations-api#redaction).
  2. Send a request to the Contact Center AI Insights API and receive a response.

  3. Optionally, use CX Insights with VPC Service Controls.




## Before you begin

Security constraints defined by your organization might prevent you from completing the following steps. For troubleshooting information, see [Develop applications in a constrained Google Cloud environment](https://docs.cloud.google.com/resource-manager/docs/organization-policy/develop-apps-constrained-environment). 

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Cloud Speech-to-Text, Cloud Storage, Contact Center AI Insights, Dialogflow, and Sensitive Data Protection (DLP) APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=speech.googleapis.com,storage.googleapis.com,contactcenterinsights.googleapis.com,dialogflow.googleapis.com,dlp.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Cloud Speech-to-Text, Cloud Storage, Contact Center AI Insights, Dialogflow, and Sensitive Data Protection (DLP) APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=speech.googleapis.com,storage.googleapis.com,contactcenterinsights.googleapis.com,dialogflow.googleapis.com,dlp.googleapis.com)




## Send a request and receive a response

  1. [Install and set up](https://docs.cloud.google.com/sdk/install) the Google Cloud CLI. You can set up the gcloud CLI in one of the following development environments:

###  Cloud Shell 

To use an online terminal with the gcloud CLI already set up, activate Cloud Shell:

At the bottom of this page, a Cloud Shell session starts and displays a command-line prompt. It can take a few seconds for the session to initialize.

###  Local shell 

To use a local development environment, follow these steps:

     1. [Install the gcloud CLI.](https://docs.cloud.google.com/sdk/docs/install)
     2. [Initialize the gcloud CLI.](https://docs.cloud.google.com/sdk/docs/initialize)

  2. Create local authentication credentials for your user account: 
         
         gcloud auth application-default login

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  3. Verify your setup by running the following command, which lists all of your CX Insights conversations.
         
         curl -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/conversations"
         

Replace the following:

     * `PROJECT_ID`: your Google Cloud project ID.
     * `LOCATION`: the [region](https://docs.cloud.google.com/gemini-enterprise-cx/insights/regionalization) in which you are running this request.

The command should return an empty dictionary: `{}`.




## Optional: Use CX Insights with VPC Service Controls

To use CX Insights with VPC Service Controls, add CX Insights to your security perimeter. For more information, see the [VPC Service Controls documentation](https://docs.cloud.google.com/vpc-service-controls/docs).

## What's next

  * [Analyze conversations using custom highlights](https://docs.cloud.google.com/gemini-enterprise-cx/insights/custom-highlights-ui)
  * [Use the console to import and analyze a conversation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/create-analyze-conversation-ui)
  * [List conversations using the console](https://docs.cloud.google.com/gemini-enterprise-cx/insights/list-conversations-ui)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
