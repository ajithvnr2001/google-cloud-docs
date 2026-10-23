---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/migrate-from-discovery-for-media/
title: Switch from Discovery for Media to media recommendations \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:12:38.215508+00:00
---

# Switch from Discovery for Media to media recommendations  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/migrate-from-discovery-for-media/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Switch from Discovery for Media to media recommendations Stay organized with collections  Save and categorize content based on your preferences. 

This page is for helping Discovery for Media users switch to media recommendations.

## What's changing?

Google is moving [Discovery for Media](https://docs.cloud.google.com/discovery-engine/media/docs/introduction) functionality to media recommendations, a capability of [Agent Search](https://docs.cloud.google.com/generative-ai-app-builder/docs/introduction#es-and-personalize).

The documents and user events that you created using Discovery for Media remain unchanged. All of your existing data and models will automatically appear in the AI Applications console, the models appearing as apps. You can manage these resources in the AI Applications console and using the API. This change means that the same user data can be used for multiple use cases, such as search and recommendations.

Existing data and models will automatically appear in the AI Applications console, with the models appearing as apps. You can manage these resources in the AI Applications console and using the API. This change means that the same user data can be used for multiple [Agent Search](https://docs.cloud.google.com/generative-ai-app-builder/docs/introduction) use cases, such as search, recommendations, and conversation.

Media recommendations functionality in the [Discovery Engine console](https://console.cloud.google.com/ai/discovery/media/dataStores/default_data_store/data/documents) is now available in the [AI Applications console](https://console.cloud.google.com/gen-app-builder/engines). The Discovery Engine console was deprecated at the end of March 2024. The API is unchanged, so your API calls will continue working after the Discovery Engine console is deprecated.

Summary of changes:

  * The API remains the same. For up-to-date reference documentation, see [APIs and reference](https://docs.cloud.google.com/generative-ai-app-builder/docs/apis) in the Agent Search documentation.

  * Media recommendations functionality in the [Discovery Engine console](https://console.cloud.google.com/ai/discovery/media/dataStores/default_data_store/data/documents) is now available in the [AI Applications console](https://console.cloud.google.com/gen-app-builder/engines).

  * The Discovery Engine console page is deprecated.

  * Models in Discovery for Media are replaced by [recommendations types](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-media-recommendations-types#model-types) in media recommendations apps. You can have one only one recommendation type per app, but you can connect multiple apps to the same data store. For more information, see [Create a media data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-media) and [Create media apps](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-app-media).

  * You can create multiple serving configs per app with different settings for recommendations demotion and recommendations diversity. However, you can't attach models to serving configs anymore.

If you have a model that is associated with multiple serving configs, Google suggests that you continue using Discovery for Media until this feature is available with media recommendations. For more information, see [Demote media recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/demote-recommendations) and [Diversify media recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/diversify-recommendations).

  * You can have multiple data stores in the same project.

  * Data stores contain both documents and user events.

  * There is no **Manual tune only** setting in media recommendations apps, as there is for models in Discovery for Media. All media recommendations apps created using Agent Search are automatically tuned every three months, and there is no setting to change this. This means that by default your apps will tune every three months. If you want to change the **Tuning status** for a model that you created in Discovery for Media, do so before Discovery for Media is deprecated.




## What's not changing?

  * All of your documents, user events, models, and settings in Discovery for Media persist in media recommendations apps and data stores.

  * All of the APIs remain the same.

  * The Discovery Engine console page will no longer be updated with new features.




## What's next?

  * Familiarize yourself with [Agent Search](https://docs.cloud.google.com/generative-ai-app-builder/docs/introduction#es-and-personalize) and [Agent Search for media](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-media).

  * Open the [AI Applications console](https://console.cloud.google.com/gen-app-builder/engines) and see how your data, models, and configurations are represented.

  * Try out media recommendations:

    * [Import data into a media data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-media).
    * [Create media apps](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-app-media).
    * [Get media recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/preview-recommendations#get-media-recommendations)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
