---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/try-enterprise-search/
title: Get started with custom search \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:35:22.250471+00:00
---

# Get started with custom search  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/try-enterprise-search/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Get started with custom search

Agent Search brings together the power of deep information retrieval, state-of-the-art natural language processing, and the latest in large language processing to understand user intent and return the most relevant results for the user.

With Agent Search, you can create apps for searching and for making recommendations. Agent Search also has special capabilities for some industries, such as media and retail.

This tutorial focuses on creating a search app for _custom_ data; that is, data which isn't specific to an industry vertical.

This tutorial explains how to create search apps for different kinds of data:

  * Website data from crawling `cloud.google.com/generative-ai-app-builder/`
  * Structured data in the form of an NDJSON-formatted dataset ingested from a Cloud Storage bucket
  * Unstructured data in the form of PDFs ingested from a Cloud Storage bucket



Before following this tutorial, make sure you have done the steps in [Before you begin](https://docs.cloud.google.com/generative-ai-app-builder/docs/before-you-begin).

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/gen-app-builder/?tutorial=generative-ai-app-builder--genappbuilder-enterprise-search-intro)

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

  4. Enable the Agent Search (Discovery Engine), BigQuery, Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=discoveryengine.googleapis.com,bigquery.googleapis.com,storage.googleapis.com)

  5. Make sure that you have the following role or roles on the project: Discovery Engine Admin 

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

  8. Enable the Agent Search (Discovery Engine), BigQuery, Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=discoveryengine.googleapis.com,bigquery.googleapis.com,storage.googleapis.com)

  9. Make sure that you have the following role or roles on the project: Discovery Engine Admin 

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

First, you'll create a data store which contains the data that your search app will index.

Click the tab for the type of data that you want to put in your data store: website, structured, or unstructured.

### Website data

  1. Go to the **Create data store** page.

[AI Applications - Create data store](https://console.cloud.google.com/gen-app-builder/data-stores/create)

  2. In the **Select a data source** pane, select **Website content**.

  3. In the **Specify the websites for your data store** pane, make sure that [**Advanced website indexing**](https://docs.cloud.google.com/generative-ai-app-builder/docs/turn-on-advanced-indexing) is turned off.

  4. In the **Sites to include** field, enter:
         
         cloud.google.com/generative-ai-app-builder/*
         

  5. Click **Continue**.

  6. In the **Configure your data store** pane, select **global (Global)** as the location for your data store.

  7. Enter a name for your data store. Note the **ID** that is generated. You'll need this later.

  8. Click **Create**.




### Structured data

  1. Go to the **Create data store** page.

[AI Applications - Create data store](https://console.cloud.google.com/gen-app-builder/data-stores/create)

  2. In the **Select a data source** pane, select **Cloud Storage**.

  3. In the **Import data from Cloud Storage** pane, select **Structured data (JSONL)**.

  4. Make sure **File** is selected.

  5. In the **`gs://`** field, enter the following value:
         
         cloud-samples-data/gen-app-builder/search/kaggle_movies/movie_metadata.ndjson
         

This Cloud Storage bucket contains an NDJSON-formatted file of movies made available by [Kaggle](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset?select=movies_metadata.csv).

  6. Click **Continue**.

  7. Assign key properties as follows:

Field name | Key property  
---|---  
`homepage` | `uri`  
`overview` | `description`  
  
And, click **Continue**.

  8. In the **Configure your data store** pane, select **global (Global)** as the location for your data store.

  9. Enter a name for your data store. Note the **ID** that is generated. You'll need this later.

  10. Click **Create**.




### Unstructured data

  1. Go to the **Create data store** page.

[AI Applications - Create data store](https://console.cloud.google.com/gen-app-builder/data-stores/create)

  2. In the **Select a data source** pane, select **Cloud Storage**.

  3. In the **Import data from Cloud Storage** pane, select **Unstructured documents (PDF, HTML, TXT and more)**.

  4. Make sure **Folder** is selected.

  5. In the **`gs://`** field, enter the following value:
         
         cloud-samples-data/gen-app-builder/search/alphabet-investor-pdfs
         

This Cloud Storage bucket contains earnings report PDFs from the [Alphabet investor site](https://abc.xyz/).

  6. Click **Continue**.

  7. In the **Configure your data store** pane, select **global (Global)** as the location for your data store.

  8. Enter a name for your data store. Note the **ID** that is generated. You'll need this later.

  9. Click **Create**.




## Create a search app

Next, you'll create a search app and link the data store you created previously.

### Website data

  1. Go to the **Create App** page.

[AI Applications - Create App](https://console.cloud.google.com/gen-app-builder/engines/create)

  2. Under **Site search with AI mode** , click **Create**.

  3. Make sure that **Enterprise edition features** is turned on.

  4. In the **Your app name** field, enter a name for your app. Your app ID appears under the app name.

  5. In the **External name of your company or organization** field, enter the company or organization name. For this tutorial, you can use `Google Cloud`, because the app will search a Google Cloud website.

  6. Select **global (Global)** as the location for your app, and then click **Continue**.

  7. In the list of data stores, select the data store that you created earlier, and then click **Create**.

  8. Go to your app's **Data** page to view the list of indexed websites and change them if needed.




### Structured data

  1. Go to the **Create App** page.

[AI Applications - Create App](https://console.cloud.google.com/gen-app-builder/engines/create)

  2. Under **Site search with AI mode** , click **Create**.

  3. Make sure that **Enterprise edition features** is turned on.

  4. In the **Your app name** field, enter a name for your app. Your app ID appears under the app name.

  5. In the **External name of your company or organization** field, enter the company or organization name. For this tutorial, you can use `Cymbal Cinemas`, because the app will search a data store of movies.

  6. Select **global (Global)** as the location for your app, and then click **Continue**.

  7. In the list of data stores, select the data store that you created earlier, and then click **Create**.

  8. On your app's **Data** page, click the **Activity** tab to see the status of your data ingestion. **Import completed** displays in the **Status** column when the import process is complete. For this dataset, this typically takes two to three minutes. You might need to click **Refresh** to see **Import completed**.

  9. Click the **Documents** tab to see the number of documents imported.




### Unstructured data

  1. Go to the **Create App** page.

[AI Applications - Create App](https://console.cloud.google.com/gen-app-builder/engines/create)

  2. Under **Site search with AI mode** , click **Create**.

  3. Make sure that **Enterprise features** is turned on.

  4. In the **Your app name** field, enter a name for your app. Your app ID appears under the app name.

  5. In the **External name of your company or organization** field, enter the company or organization name. For this tutorial, you can use `Alphabet`, because the app will search over Alphabet documents.

  6. Select **global (Global)** as the location for your app, and then click **Continue**.

  7. In the list of data stores, select the data store that you created earlier, and then click **Create**.

  8. On your app's **Data** page, click the **Activity** tab to see the status of your data ingestion. When the import process is complete, the **Status** column displays **Import completed**. For this dataset, the import process typically takes two to three minutes. You might need to click **Refresh** to see the **Import completed** status.

  9. Click the **Documents** tab to see the number of documents imported.




## Preview your app

### Website data

  1. On the **Apps** page, click the name of your new app.

  2. In the navigation menu, click **Preview** to test the search app.

  3. Optional: Click the view icons to switch between mobile view and desktop view.

  4. In the search bar, perform a search for `Agent Search` to view results about the product.




### Structured data

  1. On the **Apps** page, click the name of your new app.

  2. In the navigation menu, click **Preview** to test the search app.

  3. Optional: Click the view icons to switch between mobile view and desktop view.

  4. In the search bar, enter `trains`, and then press **Enter** to get results for movies related to trains.




### Unstructured data

  1. On the **Apps** page, click the name of your new app.

  2. In the navigation menu, click **Preview** to test the search app.

  3. Optional: Click the view icons to switch between mobile view and desktop view.

  4. In the search bar, enter `Google`, and then press **Enter** to view your results.




## Configure the search widget

  1. In the navigation menu, click **Configurations**.

  2. On the **UI** tab, configure settings for the search app.

Different UI configurations are available for different data types. For more information, see [Configure results for the search widget](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-widget-attributes).

  3. If you change configurations on the **UI** tab, click **Save and publish**.

  4. Go to the **Autocomplete** tab to configure specific settings for autocomplete.

For more information, see [Configure autocomplete](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-autocomplete).

  5. Go to the **Response Settings** tab to configure advanced features.

For more information, see [About advanced features](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-advanced-features).




## Deploy a search app

  1. On the **Apps** page, click the name of the app that you want to deploy.

  2. In the navigation menu, click **Integration**.

  3. Make sure the **Widget** tab is selected.

  4. Select **JWT or OAuth based** as the widget authorization type.

  5. In the **Domain** field, enter the domain name for web page where you'll put the widget. For example, if you are going to copy the widget to the web page `example.com/ai.html`, enter `example.com` as the domain.

  6. Click **Add** , and then click **Save**.

  7. Copy the code snippet provided in the **Copy the following code to your web application** section.

  8. In your codebase, generate an authorization token.

  9. To pass the authorization token to your widget, use the "Set authorization token" code snippet provided in the **Copy the following code to your web application** section and replace the text `<JWT or OAuth token provided by your backend>` with your authorization token.

  10. Test your deployed app. You can further adjust the configuration by following the steps "Configure the search widget". Make sure to click **Save and publish** so that the changes take effect on the deployed widget.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  1. To avoid unnecessary Google Cloud charges, use the [Google Cloud console](https://console.cloud.google.com/) to delete your project if you don't need it.
  2. If you created a new project to learn about Agent Search and you no longer need the project, [delete the project](https://console.cloud.google.com/cloud-resource-manager).
  3. If you used an existing Google Cloud project, delete the resources you created to avoid incurring charges to your account. For more information, see [Delete an app](https://docs.cloud.google.com/generative-ai-app-builder/docs/delete-engine).
  4. Follow the steps in [Turn off Agent Search](https://docs.cloud.google.com/generative-ai-app-builder/docs/turn-off-enterprise-search).



## What's next

  * [Introduction to Agent Search](https://docs.cloud.google.com/generative-ai-app-builder/docs/enterprise-search-introduction)
  * [About data, data stores, and engines](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-datastore-ingest)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
