---
url: https://docs.cloud.google.com/gemini/enterprise/docs/create-app/
title: Create an app \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:37:13.765773+00:00
---

# Create an app  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/create-app/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Create an app Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create a Gemini Enterprise app.

**Important:** If you want to use customer-managed encryption keys (CMEK) to protect your app's data, you must register your CMEK key before creating the app. Apps created prior to key registration remain unprotected. For more information, see [Customer-managed encryption keys](https://docs.cloud.google.com/gemini/enterprise/docs/cmek).**Note:** You can't connect website data stores to your Gemini Enterprise search and assistant apps.

## Create an app

### Console

  1. In the Google Cloud console, go to the **[Gemini Enterprise page](https://console.cloud.google.com/gemini-enterprise/start)**.
  2. On the **Apps** page, click **Create app**.
  3. In the **App name** field, enter a name for your app.
  4. To update the automatically generated app **ID** , click **Edit**. The app ID cannot be updated after you create the app.
  5. In the **Choose a location** section, select a **Multi-region**. Use the default **global (Global)** multi-region unless you need to restrict your data to a specific geography.
  6. Optional. Expand **Advanced options** and configure the following:

     1. In the **Company name** field, enter your company's external name, omitting suffixes such as Inc or LLC. This helps the LLM identify the company the app represents.

     2. If you are connecting a **Google Drive** data store, you can allow the app to search documents outside your organization. To enable this feature, select the **Include cross-domain documents** checkbox.

**Warning:** Enabling this feature increases security risks, such as prompt injection from external documents and manipulation of search results.
  7. Click **Create**.




### REST

Before you use the command line to create an app, you must have an existing data store. If you don't have a data store, you need to [connect a Google data source](https://docs.cloud.google.com/gemini/enterprise/docs/create-data-store) or a [third-party data source](https://docs.cloud.google.com/gemini/enterprise/docs/connect-third-party-data-source) to your app.

To use the [`engines.create`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines/create) method to create an app from the command line, follow these steps:

  1. Find your data store ID. If you already have your data store ID, skip to the next step.

     1. In the Google Cloud console, go to the **Gemini Enterprise** page and in the navigation menu, click **Data Stores**.

[Go to the Data Stores page](https://console.cloud.google.com/gemini-enterprise/data-stores)

     2. Click the name of your data store.

     3. On the **Data** page for your data store, get the data store ID.

  2. Create an app and connect it to a data store.

**Key Term:** In Gemini Enterprise, the term _app_ can be used interchangeably with the term _engine_ in the context of APIs. A Gemini Enterprise engine is a generic search engine where the `app_type` field is set to `APP_TYPE_INTRANET`.
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/engines?engineId=APP_ID" \
         -d '{
           "displayName": "APP_DISPLAY_NAME",
           "dataStoreIds": ["DATA_STORE_ENTITY_ID_1", "DATA_STORE_ENTITY_ID_2", "DATA_STORE_ENTITY_ID_3"],
           "solutionType": "SOLUTION_TYPE_SEARCH",
           "industryVertical": "GENERIC",
           "appType": "APP_TYPE_INTRANET"
         }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your project.
     * `APP_ID`: the ID of the app that you want to create.
     * `APP_DISPLAY_NAME`: the display name of the app that you want to create.
     * `DATA_STORE_ENTITY_ID`: if your data store contains entities, use the specific entity IDs. If your data store does not contain entities, use the data store ID instead.

You can include the following optional configurations in the JSON payload:

     * To provide your company's external name, include the following:
           
           "commonConfig": {
             "companyName": "COMPANY_NAME"
           }
           

Replace `COMPANY_NAME` with your company's external name, omitting suffixes such as Inc or LLC.

     * If you are connecting a **Google Drive** data store, you can allow the app to search and index documents outside your organization. To enable this feature, include the following in the JSON payload:
           
           "includeCrossDomainDocuments": true
           

**Warning:** Enabling this feature increases exposure to security risks, such as prompt injection from external documents and potential manipulation of search results.

#### Example command and result
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    -H "X-Goog-User-Project: my-project-123" \
    "https://discoveryengine.googleapis.com/v1/projects/my-project-123/locations/global/collections/default_collection/engines?engineId=my-app" \
    -d '{
      "displayName": "my-app",
      "dataStoreIds": ["slack_1234567890123_conversation", "slack_1234567890123_file", "slack_1234567890123_message"],
      "solutionType": "SOLUTION_TYPE_SEARCH",
      "industryVertical": "GENERIC",
      "appType": "APP_TYPE_INTRANET"
    }'
    
    
    * * *
    
    
    {
      "name": "projects/123456/locations/global/collections/default_collection/operations/create-engine-12345678901234567890",
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.discoveryengine.v1.Engine",
        "name": "projects/123456/locations/global/collections/default_collection/engines/my-app",
        "displayName": "my-app",
        "dataStoreIds": [
          "slack_1234567890123_conversation",
          "slack_1234567890123_file",
          "slack_1234567890123_message"
        ],
        "solutionType": "SOLUTION_TYPE_SEARCH",
        "searchEngineConfig": {
          "searchTier": "SEARCH_TIER_STANDARD"
        },
        "industryVertical": "GENERIC",
        "appType": "APP_TYPE_INTRANET"
      }
    }
    




## What's next

  * To connect an app to an existing data store, see [Connect an app to an existing data store](https://docs.cloud.google.com/gemini/enterprise/docs/connect-existing-data-store).

  * To connect your data sources, see [Connect a Google data source](https://docs.cloud.google.com/gemini/enterprise/docs/create-data-store) and [Connect a third-party data source](https://docs.cloud.google.com/gemini/enterprise/docs/connect-third-party-data-source).

  * To preview search results, go to **Configurations** > **Search UI** in the Google Cloud console or see [Get search results from StreamAssist](https://docs.cloud.google.com/gemini/enterprise/docs/get-answers-from-streamassist).

  * To configure the web app, such as to turn on and off settings like the model selector and image generator, see [Manage web app features](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
