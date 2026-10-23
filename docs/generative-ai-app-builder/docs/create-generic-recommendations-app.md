---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/create-generic-recommendations-app/
title: Create a custom recommendations app \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:13:28.222305+00:00
---

# Create a custom recommendations app  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/create-generic-recommendations-app/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Create a custom recommendations app Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This feature is a Preview offering, subject to the "Pre-GA Offerings Terms" of the [GCP Service Specific Terms](https://cloud.google.com/terms/service-terms). Pre-GA products and features may have limited support, and changes to pre-GA products and features may not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). Further, by using this feature, you agree to the [Generative AI Preview terms and conditions](https://cloud.google.com/trustedtester/aitos) ("Preview Terms"). For this feature, you can process personal data as outlined in the [Cloud Data Processing Addendum](https://cloud.google.com/terms/data-processing-addendum), subject to applicable restrictions and obligations in the Agreement (as defined in the Preview Terms). 

This page describes how to create a custom recommendations app.

### Console

To use the Google Cloud console to create a custom recommendations app, follow these steps:

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/engines)

  2. On the **Apps** page, click **Create app**.

  3. On the **Create App** page, under **Recommendations engine** , click **Create**.

  4. In the **Your app name** field, enter a name for your app. Your app ID appears under the engine name.

  5. Optional: Click **Edit** to edit your app ID.

  6. Click **Continue**.

  7. To connect to a data store, on the **Data Stores** page, select a data store that contains structured data or choose to create a data store. Do one of the following:

     * Select an existing data store, if one is available. A data store can be attached to only one app, and it can't be removed from the app later.

     * Create a new structured data store and ingest data into it. Do this by clicking **Create data store** and following the steps in the **Create a new data store** pane that opens. Then select your new data store. For more information about creating a data store, see [Create a custom recommendations data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-recommendations).

  8. Optional: To see a list of unavailable data stores, click **Learn why**.

A table is displayed with a list of data stores and the reason why they are unavailable. Here are some of the reasons why a data store might be unavailable:

     * Your data store type allows connection to only one app and the data store is already connected.
     * Your data store and your app are in different regions.
     * Your data store and your app are of different types. For example, you cannot connect a media data store to a custom recommendations app.
     * Your data store has basic website search, whereas a custom recommendations app requires a data store with advanced website indexing.
  9. Click **Create**.




### REST

Before you use the command line to create an app, you must have an existing data store. If you don't have a data store, create one following the steps in [Create a custom recommendations data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-recommendations).

**Note:** This feature is experimental.

To use the command line to create a recommendations app, follow these steps:

  1. Find your data store ID. If you already have your data store ID, skip to the next step.

     1. In the Google Cloud console, go to the **AI Applications** page and in the navigation menu, click **Data Stores**.

[Go to the Data Stores page](https://console.cloud.google.com/gen-app-builder/data-stores)

     2. Click the name of your data store.

     3. On the **Data** page for your data store, get the data store ID.

  2. Create an app and connect it to a structured data store. A data store can be attached to only one app and can't be removed from the app later.

**Key Term:** In Agent Search, the term _app_ can be used interchangeably with the term _engine_ in the context of APIs.
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/global/collections/default_collection/engines?engineId=APP_ID" \
         -d '{
           "displayName": "APP_DISPLAY_NAME",
           "dataStoreIds": ["DATA_STORE_ID"],
           "solutionType": ["SOLUTION_TYPE_RECOMMENDATION"],
           "similarDocumentsConfig": {}
         }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `APP_ID`: the ID of the recommendations app that you want to create.
     * `APP_DISPLAY_NAME`: the display name of the recommendations app that you want to create.
     * `DATA_STORE_ID`: the ID of an existing recommendations data store that you want to add to the recommendations app.



## What's next

  * To preview how your recommendations appear, see [Get recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/preview-recommendations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
