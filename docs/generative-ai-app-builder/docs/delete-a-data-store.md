---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/delete-a-data-store/
title: Delete a data store \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:38.736325+00:00
---

# Delete a data store  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/delete-a-data-store/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Delete a data store Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to delete a data store.

Deletion is an asynchronous process that can take days. You can't reuse a data store ID until the original data store is completely deleted. To prevent this from blocking your workflow, we strongly recommend that you use a unique ID for every data store. 

## Before you begin

Before deleting a structured or unstructured data store, if your data store is connected to an app, you must do one of the following:

  * To keep the app and delete only the data store, unlink the data store from its connected app.
  * To delete both the app and the data store, first [Delete the app](https://docs.cloud.google.com/generative-ai-app-builder/docs/delete-engine) that the data store is connected to.



### Structured and unstructured data stores

Before attempting to delete a structured or unstructured data store, if your data store is connected to an app, you must [delete the app](https://docs.cloud.google.com/generative-ai-app-builder/docs/delete-engine) that it is connected to.

### Website data stores

Before attempting to delete a website data store, be aware of the following:

  * **You can't delete a data store that is connected to an app.** If your data store is connected to an app, you must [delete the app](https://docs.cloud.google.com/generative-ai-app-builder/docs/delete-engine) that it is connected to.

  * **You can't delete a data store that is in the process of upgrading to[advanced website indexing](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-advanced-features#advanced-website-indexing) or downgrading to standard indexing.** You must wait for the upgrade or downgrade to complete before deleting the data store.




## Procedure

### Console

To delete a data store, follow these steps:

  1. In the Google Cloud console, go to the **AI Applications** page, and then click **Data Stores**.

[Go to the Data Stores page](https://console.cloud.google.com/gen-app-builder/data-stores)

  2. For the data store that you want to delete, click more_vert, and then click **Delete**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
