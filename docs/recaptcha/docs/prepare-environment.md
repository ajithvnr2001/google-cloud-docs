---
url: https://docs.cloud.google.com/recaptcha/docs/prepare-environment/
title: Prepare your environment for Fraud Defense \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:50:24.240793+00:00
---

# Prepare your environment for Fraud Defense  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/prepare-environment/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback 

#  Prepare your environment for Fraud Defense Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to prepare your environment to set up Google Cloud Fraud Defense.

## Before you begin

To get started with Fraud Defense, do the following:

  1. [Sign up](https://accounts.google.com/) to create a Google Account in the [Google Cloud console](https://console.cloud.google.com/security/recaptcha).

  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)




## Enable the reCAPTCHA Enterprise API

**Note:** To enable and get started with Fraud Defense on Google Cloud, you don't need to enable billing for your Google Cloud project. However, we recommend enabling billing to ensure that your site remains protected after you exceed the free monthly usage limit of Fraud Defense. For more information, see [Billing information](https://docs.cloud.google.com/recaptcha/docs/billing-information). 

### Console

  1. In the Google Cloud console, go to the **reCAPTCHA Enterprise API** page.

[Go to reCAPTCHA Enterprise API](https://console.cloud.google.com/apis/library/recaptchaenterprise.googleapis.com)

  2. Verify that the name of your project appears in the project selector at the top of the page.

If you don't see the name of your project, click the project selector, and then select your project.

  3. Click **Enable**.



### gcloud

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To set your Google Cloud project in the gcloud session, run the [`gcloud config set project`](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) command. Replace PROJECT_ID with your Google Cloud project ID. 
         
         gcloud config set project PROJECT_ID
                

  3. To enable the reCAPTCHA Enterprise API, run the [`gcloud services enable`](https://docs.cloud.google.com/sdk/gcloud/reference/services/enable) command: 
         
         gcloud services enable recaptchaenterprise.googleapis.com
                

  4. To verify that the reCAPTCHA Enterprise API is enabled, run the [`gcloud services list`](https://docs.cloud.google.com/sdk/gcloud/reference/services/list) command: 
         
         gcloud services list --enabled
                

Verify that the reCAPTCHA Enterprise API is listed in the list of enabled APIs.




## Configure roles and permissions

To get the permissions that you need to set up Fraud Defense, ask your administrator to grant you the following IAM roles on the project: 

  * [reCAPTCHA Enterprise Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.admin) (`roles/recaptchaenterprise.admin`)
  * [reCAPTCHA Enterprise Agent ](https://docs.cloud.google.com/iam/docs/roles-permissions/recaptchaenterprise#recaptchaenterprise.agent) (`roles/recaptchaenterprise.agent`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about the access control for Fraud Defense, see [Access control with IAM](https://docs.cloud.google.com/recaptcha/docs/access-control).

## What's next

  * [Understand reCAPTCHA keys](https://docs.cloud.google.com/recaptcha/docs/keys)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
