---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/demote-recommendations/
title: Demote media recommendations \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:33:27.904463+00:00
---

# Demote media recommendations  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/demote-recommendations/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Demote media recommendations Stay organized with collections  Save and categorize content based on your preferences. 

When you use media recommendations, you can demote recommendations based on viewer data or content age. Recommendations that meet the demotion criteria that you specify are demoted to the bottom of the results list. This feature is available only for media recommendations, not for custom search and recommendations.

Demotion is set on the serving config level. You can have multiple serving configs per media recommendations app, each with a different demotion setting. For more information about serving configs, see [Create and manage serving configs](https://docs.cloud.google.com/generative-ai-app-builder/docs/serving-configs).

## Demote based on viewer data

You can demote recommendations based on how an end user has recently interacted with the recommended content.

If your recommended content has a detail page, then you can demote it if the user has recently viewed it. If your content is playable media, then you can demote it depending on the amount of time the user played it or the percentage of the content that the user played.

To demote recommendations based on viewer data:

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/start)

  2. Click the name of the app that you want to configure recommendations for.

  3. Go to the **Configurations** > **Control** tab.

  4. If you have more than one serving config, select the serving config that you plan to set demotion for.

  5. In the **Recommendation demotion** section, turn on the **Demote recommendations based on viewer data** toggle to see the available demotion options.

  6. Select your demotion option and, if prompted, enter a threshold value for when to trigger demotion.

  7. Click **Save and publish**.




## Demote based on content age

You can demote playable content based on its age. You set the age threshold in days, and any content that reaches that age is demoted to the bottom of the results list.

To demote recommendations based on content age:

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/start)

  2. Click the name of the app that you want to configure recommendations for.

  3. Go to the **Configurations** > **Control** tab.

  4. If you have more than one serving config, select the serving config that you plan to set demotion for.

  5. In the **Recommendation demotion** section, turn on the **Demote recommendations based on content age** toggle.

  6. Enter a content age threshold value for when to trigger demotion.

  7. Click **Save and publish**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
