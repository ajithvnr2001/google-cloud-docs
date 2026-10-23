---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/setting-up/
title: Setup prerequisites \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:11:47.716748+00:00
---

# Setup prerequisites  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/setting-up/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Setup prerequisites Stay organized with collections  Save and categorize content based on your preferences. 

Before you can set up AI Commerce Search for a new project, you must:

  1. Create a new project or set up your existing project
  2. Enable AI Commerce Search
  3. Import your product catalog and user events



## Create a Google Cloud project

  1. On the **Manage resources** page in the Google Cloud console, select or [create a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

[Go to the Manage Resources page](https://console.cloud.google.com/cloud-resource-manager)

  2. Make sure that billing is enabled for your Cloud project. Learn how to [check if billing is enabled on a project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled).




## Set up AI Commerce Search

To use AI Commerce Search, take the following steps. Also, if you enable AI Commerce Search and use recommendations, know that costs are based on the number of queries. For more information on AI Commerce Search pricing, see [AI Commerce Search charges](https://cloud.google.com/retail/pricing).

**Important:** You must accept the Agent Search for Industry terms for every project that you want to use AI Commerce Search with.

###  For your new project 

To set up AI Commerce Search:

  1. Go to the **AI Commerce Search** page in the Google Cloud console.

[Go to the AI Commerce Search in Gemini Enterprise for Customer Experience page](https://console.cloud.google.com/ai/retail)

  2. On the **Set up AI Commerce Search** page, click **Turn on API**.

  3. When **AI Commerce Search** and **Recommendations AI** display as **On** , click **Continue**.

  4. Read the [Agent Search for Industry terms for data use](https://cloud.google.com/retail/data-use-terms) for data use and click **Accept** if you agree to the data use terms. You will receive confirmation from the Google Cloud console once the terms have been accepted for search.

  5. If you want to use the project with recommendations only, click **Get Started**.

  6. To turn on search in addition to recommendations, do the following:

     1. Click **Continue** and then click **Turn on** on the **Turn on search (Optional)** page.
     2. Click **Get Started**.

The Google Cloud console displays the AI Commerce Search components that you have turned on. You can now configure your project's initial settings.




###  For an existing project 

To continue on an existing project, complete these steps:

  1. Go to the **AI Commerce Search in Gemini Enterprise for Customer Experience** page in the Google Cloud console for your project.

[Go to the AI Commerce Search in Gemini Enterprise for Customer Experience page](https://console.cloud.google.com/ai/retail)

  2. On the **Data use terms** page, read the Discovery Solutions data use terms and click **Accept** if you agree to the terms.

  3. If you want to use the project with recommendations only, click **Get Started**.

  4. If you want to turn on search in addition to recommendations, do the following:

     1. Click **Continue** and then click **Turn on** on the **Turn on search (Optional)** page.
     2. Click **Get Started**.

**Important:** Ensure you have the Retail Admin or Owner role for your project before accepting the data use terms.

## Turn off search features

If you no longer want to use search, you can turn it off by submitting a support ticket.

To set your ticket to the correct component, select the following fields:

  * **Category** : Machine Learning
  * **Component** : AI Commerce Search: search & browse
  * **Subcomponent** : Account Administration & Billing



For more information on creating a support ticket, see [Getting support](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/getting-support).

### Turn off AI Commerce Search

You can turn off AI Commerce Search at any time by disabling it. This turns off both recommendations and search.

To turn off AI Commerce Search, complete the following steps:

  1. Go to the **AI Commerce Search API /Service Details** page in the Google Cloud console.

[Go to AI Commerce Search API Service Details page](https://console.cloud.google.com/apis/api/retail.googleapis.com)

  2. Click **Disable API**.

  3. In the **Disable AI Commerce Search API?** box, click **Disable**.


**Note:** When you disable the AI Commerce Search API, it takes several hours for the Agent Search for Industry terms for data use to be disabled for the project.

## Get started with AI Commerce Search

When you set up AI Commerce Search for a new project, the Google Cloud console displays the following three panels to help you configure your AI Commerce Search project:

  * **Data** > **Catalog** : displays your product catalog and a link to import your catalog.

  * **Data** > **Events** : displays your user events and a link to import historical user events.

  * **Serving configs** : contains details on your serving config and a link to create a new serving config.




You can use these panels to import your data and to create an initial configuration for your AI Commerce Search project.

### Import your product catalog

To import your product catalog, complete the set of steps for your data source. For more information on product catalogs, see [Importing catalog information](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/upload-catalog).

**Deprecated:** The Merchant Center connector is deprecated and only available to current users. New users must use the Catalog API or BigQuery to import catalogs.

###  Merchant Center Sync

  1. Click **Import product catalog** to open the **Import Data** panel.
  2. Choose **Product catalog**.
  3. Select **Merchant Center Sync** as your data source.
  4. Select your Merchant Center account. Check [User Access](https://support.google.com/merchants/answer/1637190) if you don't see your account.
  5. Optional: Select **Merchant Center feeds filter** to import only offers from selected feeds.  
  
If not specified, offers from all feeds are imported (including future feeds).
  6. Optional: To import only offers targeted to certain countries or languages, expand **Show Advanced Options** and select Merchant Center countries of sale and languages to filter for.
  7. Select the branch you will upload your catalog to.
  8. Click **Import**.



###  Cloud Storage 

  1. Click **Import product catalog** to open the **Import Data** panel.
  2. Choose **Product catalog** as your data source.
  3. Select the branch you will upload your catalog to.
  4. Choose **Retail Product Catalogs Schema** as the schema.
  5. Enter the Cloud Storage location of your data.
  6. If you do not have search enabled, select the product levels.  
  
You must select the product levels if this is the first time you are importing your catalog or you are re-importing the catalog after purging it. [Learn more](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/catalog#product-levels) about product levels. [Changing product levels](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/manage-catalog#change-product-levels) after you have imported any data requires a significant effort.  
  
**Important:** You can't turn on search for projects with a product catalog that has been ingested as variants.
  7. Click **Import**.



###  BigQuery 

  1. Click **Import product catalog** to open the **Import Data** panel.
  2. Choose **Product catalog**.
  3. Select **BigQuery** as your data source.
  4. Select the branch you will upload your catalog to.
  5. Choose one of the following schemas:
     * **Retail Product Catalogs Schema** : the [Product schema for AI Commerce Search](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/catalog#schema)
     * **Merchant Center** : the schema used to [bulk import from Merchant Center](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/upload-catalog#mc-rec)
  6. Enter the BigQuery table where your data is located.
  7. Optional: Under **Show advanced options** , enter the location of a Cloud Storage bucket in your project as a temporary location for your data.  
  
If not specified, a default location is used. If specified, the BigQuery and Cloud Storage bucket have to be in the same region.
  8. If you do not have search enabled and you are using the Merchant Center schema, select the product level.  
  
You must select the product level if this is the first time you are importing your catalog or you are re-importing the catalog after purging it. [Learn more](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/catalog#product-levels) about product levels. [Changing product levels](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/manage-catalog#change-product-levels) after you have imported any data requires a significant effort.  
  
**Important:** You can't turn on search for projects with a product catalog that has been ingested as variants.
  9. Click **Import**.



### Import your historical user events

To import your historical user events, complete the set of steps for your data source. For more information on historical user events, see [Importing historical user events](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/import-user-events).

**Note:** You can also record real-time user events to generate recommendations and search results. For more information, see [Recording real-time user events](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/record-events).

###  Cloud Storage 

  1. Click **Import user events** to open the **Import Data** panel.
  2. Choose **User events**.
  3. Select **Google Cloud Storage** as the data source.
  4. Choose **Retail User Events Schema** as the schema.
  5. Enter the Cloud Storage location of your data.
  6. Click **Import**.



###  BigQuery 

  1. Click **Import user events** to open the **Import Data** panel.
  2. Choose **User events**.
  3. Select **BigQuery** as the data source.
  4. Select the data schema. 

     * **Google Analytics 4** : Use for Google Analytics 4 events. 
     * **Google Analytics 360** : Use for Google Analytics 360 events, unless you are [importing events only home-page-views from Google Analytics 360](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/import-user-events#bq-ga-home-page-views-import) (in that case, use **Retail User Events Schema**). 
     * **Retail User Events Schema** : Use for importing events from sources other than Google Analytics and for [importing events only home-page-views from Google Analytics 360](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/import-user-events#bq-ga-home-page-views-import). 
  5. Enter the BigQuery table where your data is located.
  6. Optional: Enter the location of a Cloud Storage bucket in your project as a temporary location for your data.  
If not specified, a default location is used. If specified, the BigQuery and Cloud Storage bucket have to be in the same region.
  7. Optional: Under **Show advanced options** , enter the location of a Cloud Storage bucket in your project as a temporary location for your data.  
  
If not specified, a default location is used. If specified, the BigQuery and Cloud Storage bucket have to be in the same region.
  8. Click **Import**.



### Create a serving config

A [serving config](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-configs) is a serving entity that associates a model or a set of controls that are used to generate your search or recommendation results.

**Note:** AI Commerce Search creates a default serving config so this procedure is optional if you want to create a custom serving config.

To create a serving config, complete the following steps:

  1. In the **Serving configs** panel, click **Create serving config**.
  2. On the **Create Serving Config** page, choose **Search** as the product the serving configuration will be used for.
  3. Provide a name for your serving configuration.  
  
The name must be 1024 characters or less, and can contain only alphanumeric characters, underscores, hyphens, and spaces.
  4. Optional: If needed, update the ID.  
  
The ID is generated from the name you provide, and must be unique across your project. It must be 50 characters or less, and cannot contain spaces.
  5. Click **Continue**.
  6. Choose whether to enable dynamic faceting for this serving configuration.
  7. Choose or create serving controls to optimize your searches with.  
  
For more information on controls, see [Creating and managing controls.](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/manage-controls)



### Manage resources and monitor activity

When you have completed your initial configuration of your project, the Google Cloud console dashboard displays the system state of your AI Commerce Search project. The console dashboard lets you manage resources and monitor activity.

[Go to the AI Commerce Search in Gemini Enterprise for Customer Experience console](https://console.cloud.google.com/ai/retail/)

## Create an API key

An API key is required if you use a JavaScript pixel or a Tag Manager tag to capture user events from users' browsers. For more information about ways to capture user events, see [Record real-time user events](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/record-events).

To create an API key for calls to the [`userEvents.Collect`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents/collect) method, complete the following steps:

  1. Go to the Google Cloud console [Credentials](https://console.cloud.google.com/apis/credentials) page.

  2. In the project drop-down at the top of the Google Cloud console page, select your project (the project may already be selected).

  3. Click **Create credentials** and then select **API key**. _Do not add any website application restrictions_. Some user privacy settings are known to _not_ pass the referrer URL.

     * Take note of the generated API key, which you use when calling user event logging.
  4. For increased security, add an [API restriction](https://docs.cloud.google.com/docs/authentication/api-keys#adding-api-restrictions) to your API Key to restrict access to the AI Commerce Search service at `https://retail.googleapis.com/*`.


**Note:** The API key is only for authenticating the `userEvents.Collect` method. Other API methods require OAuth 2.0 through a service account or a user account.

## What's next

  * [Restrict API keys](https://docs.cloud.google.com/docs/authentication/api-keys#adding_api_restrictions)
  * [Authenticate to AI Commerce Search](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/authentication)
  * [Identity and Access Management (IAM)](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/iam)
  * [Implementing AI Commerce Search](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
