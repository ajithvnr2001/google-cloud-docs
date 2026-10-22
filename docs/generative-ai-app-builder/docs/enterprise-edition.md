---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/enterprise-edition/
title: Turn Enterprise edition on or off for search apps \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:35:31.571219+00:00
---

# Turn Enterprise edition on or off for search apps  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/enterprise-edition/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Turn Enterprise edition on or off for search apps Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to turn [Enterprise edition](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-advanced-features#enterprise-features) on or off for a search app.

Enterprise Edition is only available for search apps; it does not apply to recommendations or chat agents.

You can't turn off Enterprise edition for apps that are connected to a website data store.

## Before you begin

If you're turning on Enterprise edition features, be aware of additional costs that this can incur. See [Pricing](https://docs.cloud.google.com/generative-ai-app-builder/pricing).

Make sure that any app for which you turn off Enterprise edition doesn't require Enterprise edition features. After turning Enterprise edition off, all features that require Enterprise edition stop working in your app within a few minutes.

Features that require Enterprise edition include:

  * Website search (both Standard and Enterprise editions)

  * [Extractive answers](https://docs.cloud.google.com/generative-ai-app-builder/docs/snippets#extractive-answers)

  * [Extractive segments](https://docs.cloud.google.com/generative-ai-app-builder/docs/snippets#extractive-segments)

  * [Core generative answers](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-advanced-features#core-gen-answers)




## Turn Enterprise edition on or off

To turn Enterprise edition on or off, follow these steps:

  1. In the Google Cloud console, go to the **AI Applications > Apps** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/engines)

  2. Click the name of the app for which you want to turn Enterprise edition features on or off.

  3. In the navigation menu, click **Configurations**.

  4. Click the **Response Settings** tab.

  5. In the **Enterprise edition features** pane, click the toggle on or off. This option is only available for search apps that support enterprise edition features. This option can't be turned off for apps with website data stores.

  6. Click **Save**. Your changes take place within a few minutes.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
