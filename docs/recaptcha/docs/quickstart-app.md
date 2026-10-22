---
url: https://docs.cloud.google.com/recaptcha/docs/quickstart-app/
title: Test Google Cloud Fraud Defense in a demo website \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:13.051314+00:00
---

# Test Google Cloud Fraud Defense in a demo website  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/quickstart-app/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Test Fraud Defense in a demo website

This document shows you how to deploy a sample website integrated with Google Cloud Fraud Defense on Google Cloud to understand how Fraud Defense works.

A demo website helps you do the following:

  * Understand your users' experience with Fraud Defense.
  * Use it as a reference to integrate Fraud Defense in your own application.
  * Experiment with different frontend and backend approaches by editing the sample application source code.



You can deploy a demo website in one of the following languages: Java, Node.js, or Python.

You can deploy only one demo website at a time in a Google Cloud project.

**Note:** When you deploy a demo website, it runs on your Cloud Shell instance. Other project members cannot access or view the demo site.

## Before you begin

  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Enable the reCAPTCHA Enterprise API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=recaptchaenterprise.googleapis.com&redirect=https%3A//console.cloud.google.com)

  3. Make sure that you have the following role or roles on the project: reCAPTCHA Enterprise Admin, reCAPTCHA Enterprise Agent 

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
  4. If you have previously deployed a demo website, delete the relevant demo key.




## Deploy a demo website

  1. In the Google Cloud console, go to the demo website page.

[Go to demo website](https://console.cloud.google.com/security/recaptcha/demo)

  2. In the **Language** list, select a language.

Deployment takes about one minute.

  3. If prompted, authorize Cloud Shell to make calls using your credentials.

  4. To navigate to your new demo **Key details** page, click **View site**.

  5. To view the demo website, go to the **Frontend** card and click **View sample web page**.

The demo website opens in a separate tab.

  6. To learn the patterns for integrating Fraud Defense with your website, explore the examples.

  7. If you want to make changes to the demo website, do the following:

     1. In the **Key details** page, click **Edit source**.
     2. In the Cloud Shell Editor, find the required files in the **Explorer** and edit them as required.

The demo website automatically reloads with your saved changes.

Keep the Cloud Shell Editor open. Closing it stops Cloud Shell and the demo website.


**Warning:** Don't use the demo key in a production environment because its configuration is specific to demo environments. For instructions to create a new key, see [Create reCAPTCHA keys for websites](https://docs.cloud.google.com/recaptcha/docs/create-keys-websites).

## What's next

  * [Get started with Fraud Defense](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
