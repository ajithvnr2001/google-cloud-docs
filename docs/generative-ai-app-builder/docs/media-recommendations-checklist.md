---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/media-recommendations-checklist/
title: Media recommendations checklist \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:35:27.097267+00:00
---

# Media recommendations checklist  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/media-recommendations-checklist/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Media recommendations checklist Stay organized with collections  Save and categorize content based on your preferences. 

This page provides a checklist of the steps required to implement a media recommendations app. 

If you're new to Agent Search, consider following the [Get started with media recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/try-media-recommendations) quickstart tutorial to create a sample app. 

****

###  Set up a Google Cloud project

Set up a Google Cloud project, turn on Agent Search, and set up access control for your project. You can use an existing Google Cloud project if you have one already.

### Actions

  1. Complete the steps in [Before you begin](https://docs.cloud.google.com/generative-ai-app-builder/docs/before-you-begin).



###  Prepare your data

Prepare your data for importing to Agent Search.

Media recommendations apps require two types of data:

  * **Structured media data.** Upload metadata information about your media content, such as titles, descriptions, and URIs to the location of your media. Agent Search provides a predefined schema for media. Alternatively, you can use your own schema.

  * **User events.** Recording user events is required for media recommendations. User events are required to train your app and to generate recommendations.




### Actions

  1. Review information about media data and data stores and prepare your data according to the required schemas and fields in [About media documents and data stores](https://docs.cloud.google.com/generative-ai-app-builder/docs/media-documents). If you are using your own schema, also see [Example schema as a JSON object](https://docs.cloud.google.com/generative-ai-app-builder/docs/provide-schema#example-schema) and [structured data](https://docs.cloud.google.com/generative-ai-app-builder/docs/prepare-data#structured).

  2. Review media user event requirements in [About user events](https://docs.cloud.google.com/generative-ai-app-builder/docs/media-user-events).




###  Create your app and import your data

Create an app and data store and then import your media data and user events.

How you import media data depends on where you're importing it from. For example, if your data is in Cloud Storage, you can import it using the console or the API by providing the bucket location of your data.

### Actions

  1. [Create a media data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-media).

  2. [Create a media recommendations app](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-app-media#recs).

  3. [Bulk import historical user events](https://docs.cloud.google.com/generative-ai-app-builder/docs/import-user-events) so that your app can start training.

  4. [Set up real-time user event recording](https://docs.cloud.google.com/generative-ai-app-builder/docs/record-user-events).




###  Configure your recommendations

You can update field settings to make them filterable and filter your recommendations results using those fields.

### Actions

  1. To let Agent Search use a certain field for filtering recommendations, set that field as filterable. See [Configure field settings](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-field-settings).

  2. [Filter recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-recommendations).

  3. [Boost and bury recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/media-recommendations-boost-bury).

  4. [Diversify media recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/diversify-recommendations).

  5. Demote content if a user has recently viewed it or if the content is old. See [Demote media recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/demote-recommendations).




###  Preview recommendations

You can preview your recommendations to check if your recommendations are appearing as expected.

### Actions

  1. To preview your recommendations, use the AI Applications console or the API.

     * **Console.** Use the console **Preview** page to preview your recommendations. See the **Console** instructions for the kind of data that your app uses in [Get recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/preview-recommendations).

     * **API**. If you're integrating API calls into your application, make API calls to preview your recommendations. See the **REST** instructions for the kind of data that your app uses in [Get recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/preview-recommendations).




###  Deploy your recommendations app

When you're happy with the preview version of your media recommendations app, share it with your users by deploying it to your website.

### Actions

  1. To deploy your recommendations app, integrate API calls into your server or applications. For more information about making API calls, see the **REST** instructions for the kind of data that your app uses in [Get recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/preview-recommendations).

For client library resources, see [Agent Search client libraries](https://docs.cloud.google.com/generative-ai-app-builder/docs/libraries).




###  Maintain your app

You can maintain your app to ensure that latest and necessary data is available in your data store.

Media recommendations apps are automatically tuned every 3 months. However, if your data store undergoes significant change or if you do a bulk import of user events, you should manually retrain your app.

### Actions

  1. [Check the quality of your media data](https://docs.cloud.google.com/generative-ai-app-builder/docs/check-media-data-quality).

  2. [Refresh your structured data](https://docs.cloud.google.com/generative-ai-app-builder/docs/refresh-data#refresh-structured).

  3. [Train and tune media apps](https://docs.cloud.google.com/generative-ai-app-builder/docs/train-tune-media).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
