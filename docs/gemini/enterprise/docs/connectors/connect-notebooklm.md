---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-notebooklm/
title: Enable Gemini Notebook Enterprise as a search source (Preview) \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:36:15.845716+00:00
---

# Enable Gemini Notebook Enterprise as a search source (Preview)  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-notebooklm/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Enable Gemini Notebook Enterprise as a search source (Preview) Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This feature is a Preview offering, subject to the "Pre-GA Offerings Terms" of the [GCP Service Specific Terms](https://cloud.google.com/terms/service-terms). Pre-GA products and features may have limited support, and changes to pre-GA products and features may not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). Further, by using this feature, you agree to the [Generative AI Preview terms and conditions](https://cloud.google.com/trustedtester/aitos) ("Preview Terms"). For this feature, you can process personal data as outlined in the [Cloud Data Processing Addendum](https://cloud.google.com/terms/data-processing-addendum), subject to applicable restrictions and obligations in the Agreement (as defined in the Preview Terms). 

If your users create notebooks in Gemini Notebook Enterprise, you can enable notebooks as a search source. You create a data store of type Gemini Notebook Enterprise and attach that data store to Gemini Enterprise apps. The data from the notebooks isn't imported into the data store, but creating this notebook data store gives the app real-time access to the notebook titles in the project.

Users can then use Gemini Enterprise apps to search on notebook titles. Each user is only shown the notebooks that they created.

When creating a notebook, the following conditions apply:

  * It must be in the same project as the app.

  * Only one Gemini Notebook Enterprise data store can be attached to an app.

  * The region for the notebooks, data store, and app must be the same. For example, a notebook in the EU multi-region should be linked to a data store in the EU multi-region, which then must be connected to an app in the EU multi-region.

  * The data store is linked to all the notebooks in a given multi-region in that project.




### Console

To use the console to create a data store that makes notebooks available as search sources, follow these steps:

  1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Go to the **Data Stores** page.

  3. Click add **Create Data Store**.

  4. On the **Select a data source** page, select **Gemini Notebook**.

  5. Choose a location for your data store.

Use the same location as the notebooks that you want to make searchable.

  6. Enter a name for your data store.

  7. Click **Create**. 




## Next steps

  * Attach your data store to an app by following [Create a search app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app).

  * Preview search results after setup by following the steps in [Preview search results](https://docs.cloud.google.com/gemini/enterprise/docs/preview-search-results).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
