---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/serving-configs/
title: Create and manage media serving configs \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:13:49.892883+00:00
---

# Create and manage media serving configs  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/serving-configs/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Create and manage media serving configs Stay organized with collections  Save and categorize content based on your preferences. 

This page describes serving configs for media recommendation apps and how to create, edit, and delete them. A serving config contains configurations that are used when generating your media recommendations results.

## About serving configs

Serving configs are referenced at serving time to determine what recommendations to generate.

When any Agent Search app is created, a default serving config is also automatically created. For recommendations apps, the serving config's ID is the same as the engine ID. For search apps, the default serving config's ID is `default_search`. The default serving config ID is specified when making `recommend` or `search` API calls.

However, search and custom recommendations apps don't allow you to modify serving configs or create additional serving configs. Only media recommendation apps have modifiable serving configs and allow multiple serving configs.

For any media recommendations app, you can create multiple serving configs with different settings for recommendations boost/bury, demotion, and diversity. To get recommendations from a specific serving config with the boost/bury, demotion, and diversity settings that you need, specify that serving config's ID in the `recommend` request.

## Serving config settings

The following settings are available for serving configs:

  * **Recommendation boost/bury**. You can boost or bury media recommendations based on a filter and boost value. For information about boosting and burying media recommendations, [Boost and bury media recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/media-recommendations-boost-bury).

**Note:** Boost/bury controls can only be created through the API. They can't be created using Google Cloud console.
  * **Recommendation demotion**. You can demote media recommendations based on viewer data or content age. For information about demotion settings and how to set them, see [Demote media recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/demote-recommendations).

  * **Recommendation diversity**. You can diversify recommendations to reduce the likelihood that similar content is shown in a recommendation panel. For information about diversification settings and how to set them, see [Diversify media recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/diversify-recommendations).




## Create a serving config

To create a serving config, follow these steps:

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/engines)

  2. Click the name of the app for which you will create a serving config.

  3. Go to the **Configurations** > **Control** tab.

  4. Click **Create new serving config**.

  5. Enter a name for your serving config.

  6. Set configurations for recommendations: demotion and diversity.

For more information about these settings, see [Demote media recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/demote-recommendations), and [Diversify media recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/diversify-recommendations).

  7. Click **Save and publish**.




## Edit a serving config

To edit a serving config, follow these steps:

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/engines)

  2. Click the name of the app whose serving config you want to edit.

  3. Go to the **Configurations** > **Control** tab.

  4. If you have more than one serving config, click the name of the serving config that you want to edit.

  5. Update your configurations for recommendation demotion or diversity.

For more information about these settings, see [Demote media recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/demote-recommendations) and [Diversify media recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/diversify-recommendations).

  6. Click **Save and publish**.




## Delete a serving config

You can delete a serving config only if you have multiple serving configs.

To delete a serving config, follow these steps:

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/engines)

  2. Click the name of the app whose serving config you will delete.

  3. Go to the **Configurations** > **Control** tab.

  4. For the serving config you that want to delete, click more_vert, and then click **Delete**.

  5. In the confirmation dialog, type the name of the serving config to delete, and then click **Confirm**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
