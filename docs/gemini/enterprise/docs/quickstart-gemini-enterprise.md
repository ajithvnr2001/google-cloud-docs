---
url: https://docs.cloud.google.com/gemini/enterprise/docs/quickstart-gemini-enterprise/
title: Get started with Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:49:46.217151+00:00
---

# Get started with Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/quickstart-gemini-enterprise/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Get started with Gemini Enterprise

To see an example of how to get started with Gemini Enterprise, run the "Intro to Gemini Enterprise" notebook in one of the following environments: 

[![](https://docs.cloud.google.com/static/vertex-ai/images/colab-logo-32px.png)Open in Colab](https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/search/gemini-enterprise/intro_gemini_enterprise.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/github-logo-32px.png)View on GitHub](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/search/gemini-enterprise/intro_gemini_enterprise.ipynb)

Gemini Enterprise brings together the power of deep information retrieval, state-of-the-art natural language processing, and the latest in large language processing to understand user intent and return the most relevant results for the user.

Before following this tutorial, make sure you have done the steps in [Before you begin](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin).

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/gemini-enterprise/?tutorial=gemini-enterprise--gemini-enterprise-intro)

* * *

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Gemini Enterprise (Discovery Engine), Cloud Storage, Identity and Access Management APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com,discoveryengine.googleapis.com,storage.googleapis.com,iam.googleapis.com)

  5. Make sure that you have the following role or roles on the project: Gemini Enterprise Admin 

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

  6. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  7. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  8. Enable the Gemini Enterprise (Discovery Engine), Cloud Storage, Identity and Access Management APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com,discoveryengine.googleapis.com,storage.googleapis.com,iam.googleapis.com)

  9. Make sure that you have the following role or roles on the project: Gemini Enterprise Admin 

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




## Create a Gemini Enterprise app

  1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Click **Create app**.

  3. Under **Your app name** , enter a name for your app. Your app ID appears under the app name.

  4. Select **global (Global)** as the location for your app.

  5. Under **External name of your company or organization** , enter the company or organization name. For this tutorial, you can use `Cymbal Bank`.

  6. Click **Create**.




Once the app is created, you are redirected to the **Overview** page of your app.

### Create a data store

  1. Under **Complete your setup** , click **Create Data Store**.

  2. Under **Cloud Storage** , click **Select**.

  3. Under **Unstructured Data Import (Document Search & RAG)**, make sure **Documents** is selected.

  4. Under **Synchronization frequency** , make sure **One time** is selected.

  5. Under **Select a folder or a file you want to import** , make sure **Folder** is selected.

  6. Enter the following value in the **`gs://`** field:
         
         cloud-samples-data/gen-app-builder/search/cymbal-bank-employee
         

This Cloud Storage bucket contains PDF files for internal use by a fictional bank, Cymbal Bank.

  7. Click **Continue**.

  8. Under **Your data store name** , enter a name for your data store, and then click **Create**.

The Google Cloud console redirects you to the Connected data stores page, and it shows the data store you just created.




## Preview your app

**Note:** Because it takes a few minutes for the data stores to index and sync with the app, the preview isn't available immediately.

  1. In the navigation menu, click **Overview** to return to the overview page.

  2. Under **Your Gemini Enterprise webapp is ready** , click the link to visit the web app.

  3. To test the imported data, click **Connectors** and make sure that **Google Search** is not selected.

![Connectors button](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/assistant/assistant-actions-authorize.png)

  4. In the search bar, ask a question about the data that we imported; for example, ask `How do I book business travel?`

If the answer to this question doesn't specifically reference Cymbal Bank, wait a few more minutes and try again.

  5. Ask additional questions such as: `Who founded Cymbal Bank?` or `Where are the headquarters of Cymbal Bank?`




## Configure the search web app

  1. Return to the Google Cloud console.

  2. In the navigation menu, click **Configurations**.

  3. On the **Search UI** tab, configure settings for the search app.

  4. Under **Appearance and branding options** change the logo to this one for **Cymbal Bank**.
         
         https://storage.googleapis.com/cloud-samples-data/gen-app-builder/search/cymbal-bank-logo.png
         

  5. If you change configurations on the **UI** tab, click **Save and publish**.

  6. Go to the **Autocomplete** tab to configure specific settings for autocomplete.

Set **Enable autocomplete** to **Now** and expect to wait a day or two before you see autocomplete suggestions.

  7. Go to the **Assistant** tab to configure settings for the search assistant.

On this page, you can set additional LLM system instructions, enable Model Armor, web grounding, and other settings related to the default assistant.




## View the search web app

To view your Gemini Enterprise web app, do the following:

  1. In the navigation menu, click **Integration**.

  2. Make sure that **Enable the Web App** is enabled.

  3. In the **The link to your web app** section, click **Copy** and open the link in your browser.

  4. Optional: Share the search app with your users by copying the URL and sending it to them. Users can bookmark the web app URL for access.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  1. To avoid unnecessary Google Cloud charges, use the [Google Cloud console](https://console.cloud.google.com/) to delete your project if you don't need it.
  2. If you created a new project to learn about Gemini Enterprise and you no longer need the project, [delete the project](https://console.cloud.google.com/cloud-resource-manager).
  3. If you used an existing Google Cloud project, delete the resources you created to avoid incurring charges to your account. For more information, see [Delete an app](https://docs.cloud.google.com/gemini/enterprise/docs/delete-app) and [delete a data store](https://docs.cloud.google.com/gemini/enterprise/docs/delete-a-data-store).
  4. Follow the steps in [Turn off Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/turn-off-gemini-enterprise).



## What's next

  * Learn more about [Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/overview).
  * Learn more [about apps and data stores](https://docs.cloud.google.com/gemini/enterprise/docs/apps-data-stores).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
