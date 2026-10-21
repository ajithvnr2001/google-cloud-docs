---
url: https://docs.cloud.google.com/document-warehouse/docs/regions/
title: Regional and multi-regional support \u00a0|\u00a0 Document AI Warehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:42:41.671596+00:00
---

# Regional and multi-regional support  |  Document AI Warehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-warehouse/docs/regions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI Warehouse ](https://docs.cloud.google.com/document-warehouse/docs)
  * [ Reference ](https://docs.cloud.google.com/document-warehouse/docs/reference/rest)



Send feedback 

#  Regional and multi-regional support Stay organized with collections  Save and categorize content based on your preferences. 

**Caution** : Document AI Warehouse is deprecated and will no longer be available on Google Cloud after January 16, 2025. To safeguard your data, migrate any documents currently saved in Document AI Warehouse to an alternative like Cloud Storage. Verify that your data migration is completed before the discontinuation date to prevent any data loss. See [Deprecations](https://docs.cloud.google.com/document-warehouse/docs/deprecations) for details.

You must specify either a regional or multi-regional [location](https://cloud.google.com/about/locations) for data storage and document processing.

Document AI Warehouse supports the following multi-region locations:

  * `us` (United States)
  * `eu` (Europe)



## Locations

Document AI Warehouse offers you some control over where the resources for your project are stored and processed. In particular, when you [provision and initialize the resources](https://docs.cloud.google.com/document-warehouse/docs/quickstart), you must choose a location to store and process your data.

By default Document AI Warehouse stores and processes resources in a **US** location. If you choose the **European Union** location, Google will store your data and process it only in the European Union. You and your users can access the data from any location.

## Setting the location using the API

You must specify your processor's location whenever you send a processing request via the API.

For example, if your processor is configured to store and process your data in the European Union, then use the URI `eu-contentwarehouse.googleapis.com`:

Method / endpoint format | `Create document` | 

  * `https://eu-contentwarehouse.googleapis.com/v1/projects/$PROJECT_ID/locations/eu/documents`

  
---|---  
`Search document` | 

  * `https://eu-contentwarehouse.googleapis.com/v1/projects/$PROJECT_ID/locations/eu/documents:search`

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
