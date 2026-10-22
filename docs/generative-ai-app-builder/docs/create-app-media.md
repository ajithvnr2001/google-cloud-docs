---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/create-app-media/
title: Create media apps \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:35:14.785210+00:00
---

# Create media apps  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/create-app-media/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Create media apps Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create media recommendation apps and media search apps.

The processes for creating media recommendations apps and creating media search apps are similar. Both apps can use the same media data stores—although when you create a media recommendations app, you must choose a recommendations type and a business objective for your app.

## Before you begin

Make sure that you have created your media data store.

For information about creating a media data store, see [Create a media data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-media).

## Create a media recommendations app

To use the Google Cloud console to create a media recommendations app, follow these steps:

### Console

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/engines)

  2. On the **Apps** page, click **Create app**.

  3. On the **Create app** page, under **Media recommendations** , click **Create**.

  4. In the **App name** field, enter a name for your app. Your app ID, also called the engine ID, appears under the field.

  5. Optional: Click **Edit** to edit your app ID.

  6. Select a recommendations type. For more information, see [Recommendations types](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-media-recommendations-types).

  7. Select a business objective. For more information, see [Optimization for business objectives](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-media-recommendations-types#opt-obj).

  8. (Only for Recommended for you) Select a context event type. For more information, see [Recommended for you](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-media-recommendations-types#recommended-for-you).

  9. (Only for Most popular) Enter a time window in the **Days** field if you selected the **Most popular** recommendations type.

  10. Click **Continue**.

  11. Select a media data store that you previously created. Only media data stores are displayed for selection.

  12. Optional: To see a list of unavailable data stores, click **Learn why**.

A table is displayed with a list of data stores and the reason why they are unavailable.

  13. On the **Data Stores** page, click **Create**. Your new app is created and connected to the data store that you selected. The information page for your data store appears.

  14. Check the quality of the data in your data store:

     1. Click **Data quality**. If you see the message **Data requirements not met** , you have to import more data, usually in the form of more recent user events. For information about importing user events, see [About media user events](https://docs.cloud.google.com/generative-ai-app-builder/docs/media-user-events) and [Import historical user events](https://docs.cloud.google.com/generative-ai-app-builder/docs/import-user-events), and [Record real-time user events](https://docs.cloud.google.com/generative-ai-app-builder/docs/record-user-events). After importing data, it can take some time for the **Requirements** tab to update its status.

     2. To review additional quality metrics about your data, click **Optimization**. For more information, see [Check data quality for media recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/check-media-data-quality). 




**Note:** It can take two to five days for your app to train and be ready for queries.

## Create a media search app

To use the Google Cloud console to create a media search app, follow these steps:

### Console

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/engines)

  2. On the **Apps** page, click **Create app**.

  3. On the **Create App** page, under **Media search** , click **Create**.

  4. In the **App name** field, enter a name for your app. Your app ID, also called the engine ID, appears under the field.

  5. Optional: Click **Edit** to edit your app ID.

  6. Click **Continue**.

  7. Select a media data store that you previously created. Only media data stores are displayed for selection.

  8. Optional: To see a list of unavailable data stores, click **Learn why**.

A table is displayed with a list of data stores and the reason why they are unavailable.

  9. On the **Data Stores** page, click **Create**. Your new app is created and connected to the data store that you selected. The information page for your data store appears.




## What's next

  * For search apps: [Configure search results for structured data](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-widget-attributes#configure_search_structured)

  * For recommendations apps: [Get media recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/preview-recommendations#get-media-recommendations)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
