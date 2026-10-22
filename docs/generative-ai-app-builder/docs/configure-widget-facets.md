---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-widget-facets/
title: Configure facets for the search widget \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:34.034829+00:00
---

# Configure facets for the search widget  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-widget-facets/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Configure facets for the search widget Stay organized with collections  Save and categorize content based on your preferences. 

Facets can be shown next to results in the search widget to help users filter the results. You can use the **Configurations** page in the Google Cloud console to specify which fields to use as facets on your widget for apps with structured data or unstructured data with metadata.

Facet configuration is not supported for widgets for apps with website data or unstructured data without metadata.

If you use access control for your data sources, these configuration settings also apply to the web app.

Before setting a field as a facet, make sure that the field is set to **Retrievable** and **Indexable**. For more information, see [Configure field settings](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-field-settings).

To set a field as a facet:

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/start)

  2. Click the name of the app that you want to edit.

  3. Click **Configurations**.

  4. Click the **UI** tab.

  5. If you have multiple data stores connected to your app, select the data store to configure facet settings for.

  6. Expand the **Facet settings** section.

  7. Click **Add facet**.

  8. Select a field to use as a facet.

  9. Enter a display name for the facet.

  10. Click **Save and publish**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
