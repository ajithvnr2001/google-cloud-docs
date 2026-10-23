---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/turn-off-enterprise-search/
title: Turn off Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:13:24.350308+00:00
---

# Turn off Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/turn-off-enterprise-search/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Turn off Agent Search Stay organized with collections  Save and categorize content based on your preferences. 

You can turn off Agent Search by disabling the Discovery Engine API. Disabling the Discovery Engine API has the following effects:

  * All Gemini Enterprise and Agent Search resources might be deleted
  * Charges might continue to appear for up to a day after disabling the API



Because Agent Search and Gemini Enterprise are based on the Discovery Engine API, disabling the Discovery Engine API turns off all these products and any code that calls the Discovery Engine API fails.

To disable the Discovery Engine API, follow these steps:

  1. In the Google Cloud console, go to the [**Discovery Engine API Service Details**](https://console.cloud.google.com/apis/api/discoveryengine.googleapis.com) page.
  2. Click **Disable API**.
  3. In the **Disable Discovery Engine API?** box, click **Disable**.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
