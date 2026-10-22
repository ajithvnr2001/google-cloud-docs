---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/locations/
title: Agent Search locations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:28.528194+00:00
---

# Agent Search locations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/locations/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)
  * [ Resources ](https://docs.cloud.google.com/generative-ai-app-builder/docs/resources)



Send feedback 

#  Agent Search locations Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the locations where Agent Search is available.

Agent Search supports data residency at-rest when using multi-region APIs as described below.

If you don't have security, compliance, or regulatory reasons to locate your data in the US or EU multi-region, Google recommends that you choose the `global` location. This is because the global location provides better end-user response times and the full feature set. See Limitations for multi-regions.

## Multi-regions

The following table lists the multi-regions where Agent Search is available.

Multi-region description | Multi-region name  
---|---  
API availability in the European Union | `eu`  
API availability in the United States | `us`  
**Important:** All machine learning (ML) processes, such as training, prediction, and tuning a model, occur within the US when requests are made to regionally-available APIs in the US, or within the EU when requests are made to regionally-available APIs in Europe.

## Specify a multi-region for your data store

To confine your at-rest data to the US or EU multi-region, follow these steps:

  1. If you create the data store through the Google Cloud console, then choose **us (multiple regions in the United States)** or **eu (multiple regions in the European Union)** when you pick your app location.

For more information, see [Create a search app](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-engine-es).

  2. For API calls, replace `discoveryengine` with `eu-discoveryengine` or `us-discoveryengine` and replace `global` with `eu` or `us`.

For example, the path for the calls is:
         
         https://**eu-** discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/**eu** /…

or
         
         https://**us-** discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/**us** /…

instead of
         
         https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/**global** /…

  3. Review the limitations associated with using a specific multi-region.




## Limitations for multi-regions

The following features of Agent Search are supported globally but are not supported for the US and EU multi-regions or are supported in the multi-regions in Preview:

  * **Autocomplete** : Although autocomplete is available in the US and EU multi-regions, the tail match suggestions and the advanced document data mode features cannot be used in multi-regions. For general information about autocomplete, see [Configure autocomplete](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-autocomplete).

  * **Basic website search:** For website data stores, you must use advanced website indexing. Basic website search is not available. For general information about Advanced website indexing, see [Advanced website indexing](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-advanced-features#advanced-website-indexing).

  * **User events:** User events don't affect search results.

  * **Dynamic facets:** Even if a field is set to **Dynamic Facetable** , Agent Search does not use that field as a dynamic facet.

  * **Analytics:** Search analytics are available in Public preview in US and EU multi-regions. Viewing media recommendations analytics is global only. For general information about analytics, see [View analytics](https://docs.cloud.google.com/generative-ai-app-builder/docs/view-analytics).

  * **Media:** Media data stores are global only. You can't create media data stores for the US or EU multi-regions. For general information about media data stores, see [Create media apps and data stores](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-app-media) and [About media documents and data stores](https://docs.cloud.google.com/generative-ai-app-builder/docs/media-documents).




Using multi-region APIs might not produce identical results to the global API. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
