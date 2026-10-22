---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/turn-on-advanced-indexing/
title: Turn on advanced website indexing \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:35:21.595394+00:00
---

# Turn on advanced website indexing  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/turn-on-advanced-indexing/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Turn on advanced website indexing Stay organized with collections  Save and categorize content based on your preferences. 

Turning on [advanced website indexing](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-advanced-features#advanced-website-indexing) generates an index for the websites that you specify when you create your data store. You can turn on advanced website indexing in the following situations:

  * When you create a data store for website search. The data store creation process lets you turn on advanced website indexing.
  * When you upgrade your data store from basic website search to advanced website indexing.



A data store is indexed using advanced website indexing only after a successful [domain verification](https://docs.cloud.google.com/generative-ai-app-builder/docs/domain-verification). Using advanced website indexing imposes a quota on the number of pages that you can index. You can [upgrade this quota](https://docs.cloud.google.com/generative-ai-app-builder/quotas#quota-for-webpage-indexing) if necessary. Advanced website indexing incurs [additional cost](https://docs.cloud.google.com/generative-ai-app-builder/pricing). For more information, see [Advanced website indexing](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-advanced-features#advanced-website-indexing).

You cannot turn off advanced website indexing for an existing data store. Instead, you must create a new data store, and during the data store creation process, don't select the **Advanced website indexing** option.

To turn on advanced website indexing for an existing data store that uses basic website search, follow these steps:

  1. In the Google Cloud console, go to the **Agent Search** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/engines)

  2. In the navigation menu, click **Data Stores**.

  3. Click the data store for which you want to turn on advanced website search.

  4. On your data store page, in the **Type** row, click **Upgrade**.

  5. In the **Verify your domains** pane, verify the domains either by domain association or by verifying domain ownership. For more information, see [Verify website domains](https://docs.cloud.google.com/generative-ai-app-builder/docs/domain-verification).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
