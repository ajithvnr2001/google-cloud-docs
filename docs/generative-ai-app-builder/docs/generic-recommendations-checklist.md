---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/generic-recommendations-checklist/
title: Custom recommendations checklist \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:35:29.658881+00:00
---

# Custom recommendations checklist  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/generic-recommendations-checklist/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Custom recommendations checklist Stay organized with collections  Save and categorize content based on your preferences. 

This page provides a checklist of the steps required to create a generic recommendations app. 

If you're new to Agent Search, consider following the [Get started with custom recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/try-generic-recommendations) tutorial to create a sample app. 

****

###  Set up a Google Cloud project

Set up a Google Cloud project, turn on Agent Search, and set up access control for your project. You can use an existing Google Cloud project if you have one already.

### Actions

  1. Review [Before you begin](https://docs.cloud.google.com/generative-ai-app-builder/docs/before-you-begin) and confirm that you have completed the steps.



###  Prepare your data

Prepare your data for importing to Agent Search.

For custom recommendations, you must supply **structured data**. This is data provided with a specific schema. For example, you can provide data in a BigQuery table or as JSON files in Cloud Storage.

### Actions

  1. Review the information about supported data and the relationship between apps and data stores in [About apps and data stores](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-datastore-ingest).

  2. Prepare your data according to the requirements in [Prepare data for ingestion](https://docs.cloud.google.com/generative-ai-app-builder/docs/prepare-data#structured).




###  Import your data

Create a data store and then import your data into it.

How you import your data depends on where you're importing it from. For example, if your data is in Cloud Storage, you can import it using the console or the API by providing the bucket location of your data.

### Actions

  1. Follow the instructions for your data source in [Create a custom recommendations data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-recommendations).



###  Create your app

Create your custom recommendations app and connect it to your new data store.

### Actions

  1. [Create a custom recommendations app](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-generic-recommendations-app).



###  Configure your recommendations

You can update field settings to make them filterable and filter your recommendations results using those fields.

### Actions

  1. Set specific fields as filterable to allow Agent Search to use those fields for filtering recommendations. See [Configure field settings](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-field-settings).

  2. [Filter recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-recommendations).




###  Preview recommendations

You can preview your recommendations to check if your recommendations are appearing as expected.

### Actions

  1. To preview your recommendations, use the Agent Search console or the API.

     * **Console.** Use the console **Preview** page to preview your recommendations. See the **Console** instructions for the kind of data that your app uses in [Get recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/preview-recommendations).

     * **API**. If you're integrating API calls into your application, make API calls to preview your recommendations. See the **REST** instructions for the kind of data that your app uses in [Get recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/preview-recommendations).




###  Deploy your recommendations app

When you are happy with the previews from your recommendations app, share it with your users by deploying it to your website.

### Actions

  1. To deploy your recommendations app, integrate API calls into your server or applications. For more information about making API calls, see the **REST** instructions for the kind of data that your app uses in [Get recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/preview-recommendations).

For client library resources, see [Agent Search client libraries](https://docs.cloud.google.com/generative-ai-app-builder/docs/libraries).




###  Record and import user events

To get personalized recommendation results, you can update the user events in your recommendation app. For more information see [About user events](https://docs.cloud.google.com/generative-ai-app-builder/docs/user-events).

### Actions

  1. [Import historical user events](https://docs.cloud.google.com/generative-ai-app-builder/docs/import-user-events).
  2. [Record real-time user events](https://docs.cloud.google.com/generative-ai-app-builder/docs/record-user-events).



###  Maintain your app

You can maintain your app to ensure that latest and necessary data is available in your data store.

### Actions

  1. [Refresh your data](https://docs.cloud.google.com/generative-ai-app-builder/docs/refresh-data).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
