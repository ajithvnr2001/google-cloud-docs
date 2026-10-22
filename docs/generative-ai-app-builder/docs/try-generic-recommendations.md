---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/try-generic-recommendations/
title: Get started with custom recommendations \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:35:22.505818+00:00
---

# Get started with custom recommendations  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/try-generic-recommendations/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Get started with custom recommendations

**Note:** This feature is a Preview offering, subject to the "Pre-GA Offerings Terms" of the [GCP Service Specific Terms](https://cloud.google.com/terms/service-terms). Pre-GA products and features may have limited support, and changes to pre-GA products and features may not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). Further, by using this feature, you agree to the [Generative AI Preview terms and conditions](https://cloud.google.com/trustedtester/aitos) ("Preview Terms"). For this feature, you can process personal data as outlined in the [Cloud Data Processing Addendum](https://cloud.google.com/terms/data-processing-addendum), subject to applicable restrictions and obligations in the Agreement (as defined in the Preview Terms). 

You can quickly build a state-of-the-art custom recommendations app on your own data that can suggest content similar to the content that the user is currently viewing.

This tutorial explains how to create a custom recommendations app for structured data. In this case, the structured data is in the form of NDJSON ingested from a Cloud Storage bucket.

Before following this tutorial, make sure you have done the steps in [Before you begin](https://docs.cloud.google.com/generative-ai-app-builder/docs/before-you-begin).

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/gen-app-builder/?tutorial=generative-ai-app-builder--genappbuilder-recommendations-intro)

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

  4. Enable the Agent Search (Discovery Engine), Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=discoveryengine.googleapis.com,storage.googleapis.com)

  5. Make sure that you have the following role or roles on the project: Discovery Engine Admin, Monitoring Viewer, and Service Usage Viewer. 

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

  8. Enable the Agent Search (Discovery Engine), Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=discoveryengine.googleapis.com,storage.googleapis.com)

  9. Make sure that you have the following role or roles on the project: Discovery Engine Admin, Monitoring Viewer, and Service Usage Viewer. 

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




## Enable Agent Search

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/start)

  2. Optional: Click **Allow Google to selectively sample model input and responses**.

  3. Click **Continue and activate the API**.




## Create a data store

This procedure guides you through creating a data store and uploading sample data provided.

  1. Go to the **Data Stores** page.

  2. Click **Create data store**.

  3. On the **Select a data source** page, select **Cloud Storage**.

  4. On the **Import data from Cloud Storage** page, select **Structured data (JSONL)**.

  5. Click **File**.

  6. In the **gs://** field, enter the following value:
         
         cloud-samples-data/gen-app-builder/search/kaggle_movies/movie_metadata.ndjson
         

This Cloud Storage bucket contains an NDJSON-formatted file of movies made available by [Kaggle](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset?select=movies_metadata.csv).

  7. Click **Continue**.

  8. Assign key properties as follows:

Field name | Key property  
---|---  
`homepage` | `uri`  
`overview` | `description`  
  
And, click **Continue**.

  9. Enter a display name for your data store, and then click **Create**.

  10. Click the name of your data store.

  11. On the **Data** page, go to the **Activity** tab to see the status of your data ingestion. **Import completed** displays in the **Status** column when the import process is complete. For this dataset, this typically takes two to three minutes. You might need to click **Refresh** to see **Import completed**.

  12. Click the **Documents** tab to see the imported documents.




## Create an app

Next, you create a recommendations app and link the data store you created previously.

  1. Go to the **Apps** page.

  2. Click **Create app**.

  3. On the **Create App** page, under **Recommendations engine** , click **Create**.

  4. In the **App name** field, enter a name for your app. Your app ID appears under the app name.

  5. Click **Continue**.

  6. In the list of data stores, select the data store that you created earlier.

  7. Click **Create**.




### Preview your app

  1. In the navigation menu, click **Preview** to test the app.

  2. If you see the message "You will be able to preview your recommendation engine here We are still preparing your engine, please check back later", wait and periodically refresh the page. You might have to wait some hours or until the next day to preview your data.

  3. Click the **Document ID** field. A list of document IDs appears.

  4. Click the document ID for the document that you want recommendations for. Alternatively, enter a document ID into the **Document ID** field.

  5. Click **Get recommendations**. A list of recommended documents appears.

  6. Click a document to get document details.




### Deploy your app

There is no recommendations widget for deploying your app. To test your app before deployment:

  1. Go to the **Data** page and copy a document **ID**.

  2. Go to the **Integration** page. This page includes a sample command for the [`servingConfigs.recommend`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.dataStores.servingConfigs/recommend) method in the REST API.

  3. Paste the document ID you copied earlier into the **Document ID** field.

  4. Leave the **User Pseudo ID** field as is.

  5. Copy the example request and run it in Cloud Shell.

The results are the IDs of documents recommended based on the document that you chose.




For help integrating the recommendations app into your web app, see the code samples for C#, Go, Java, Node.js, PHP, and Ruby at [Get recommendations for an app](https://docs.cloud.google.com/generative-ai-app-builder/docs/preview-recommendations).

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  1. To avoid unnecessary Google Cloud charges, use the [Google Cloud console](https://console.cloud.google.com/) to delete your project if you don't need it.
  2. If you created a new project to learn about Agent Search and you no longer need the project, [delete the project](https://console.cloud.google.com/cloud-resource-manager).
  3. If you used an existing Google Cloud project, delete the resources you created to avoid incurring charges to your account. For more information, see [Delete an app](https://docs.cloud.google.com/generative-ai-app-builder/docs/delete-engine).
  4. Follow the steps in [Turn off Agent Search](https://docs.cloud.google.com/generative-ai-app-builder/docs/turn-off-enterprise-search).



## What's next

  * [Introduction to Agent Search](https://docs.cloud.google.com/generative-ai-app-builder/docs/enterprise-search-introduction)
  * [About apps and data stores](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-datastore-ingest)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
