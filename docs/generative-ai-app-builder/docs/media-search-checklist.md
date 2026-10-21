---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/media-search-checklist/
title: Media search checklist \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:28:00.181326+00:00
---

# Media search checklist  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/media-search-checklist/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Media search checklist Stay organized with collections  Save and categorize content based on your preferences. 

This page provides a checklist of the steps required to implement a media search app. 

If you're new to Agent Search, consider following the [Get started with media search](https://docs.cloud.google.com/generative-ai-app-builder/docs/try-media-search) quickstart tutorial to create a sample app.

****

###  Set up a Google Cloud project

Set up a Google Cloud project, turn on Agent Search, and set up access control for your project. You can use an existing Google Cloud project if you have one already.

### Actions

  1. Complete the steps in [Before you begin](https://docs.cloud.google.com/generative-ai-app-builder/docs/before-you-begin).



###  Prepare your data

Prepare your data for importing to Agent Search.

Media search apps use the following data:

  * **Structured media data.** Required. Upload metadata information about your media content, such as titles, descriptions, and URIs to the location of your media. Agent Search provides a predefined schema for media. Alternatively, you can use your own schema.

  * **User events.** Required. User events help rank search results.




### Actions

  1. Review information about media data and data stores and prepare your data according to the required schemas and fields in [About media documents and data stores](https://docs.cloud.google.com/generative-ai-app-builder/docs/media-documents). If you are using your own schema, also see [Example schema as a JSON object](https://docs.cloud.google.com/generative-ai-app-builder/docs/provide-schema#example-schema) and [structured data](https://docs.cloud.google.com/generative-ai-app-builder/docs/prepare-data#structured).

  2. Review media user event requirements in [About media user events](https://docs.cloud.google.com/generative-ai-app-builder/docs/media-user-events).




###  Create your app and import your data

Create an app and data store and then import your media data.

How you import media data depends on where you're importing it from. For example, if your data is in Cloud Storage, you can import it using the console or the API by providing the bucket location of your data.

### Actions

  1. [Create a media data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-media).

  2. [Create media apps](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-app-media).

  3. [Bulk import historical user events](https://docs.cloud.google.com/generative-ai-app-builder/docs/import-user-events) so that your app can start training.

  4. [Set up real-time user event recording](https://docs.cloud.google.com/generative-ai-app-builder/docs/record-user-events).




###  Configure your search settings

Agent Search provides many configuration options. Some options depend on whether you plan to deploy a search widget.

### Actions

Depending on your use case and whether you plan to deploy the out-of-the-box search widget or integrate search API calls into your own code, Agent Search provides several options for configuration.

  1. You can embed a search widget into your website that automatically provides a search bar and expandable search interface. If you plan to deploy the search widget, configure the following:

     * **Search widget results.** See [Configure results for the search widget](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-widget-attributes).

     * **Search widget facets.** See [Configure facets for the search widget](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-widget-facets).

  2. If you plan to integrate search API calls into your server or application instead of using the widget, you can configure your search settings using the following options:

     * **Field settings.** For structured data or for unstructured data with metadata, update field settings to refine how Agent Search uses metadata for search. See [Configure fields for search](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-search-attributes).

     * **Autocomplete.** Depending on your data, set up autocomplete suggestions based on document content, fields, search history, or user events. See [Configure autocomplete](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-autocomplete).

     * **Serving controls.** Control when search results are boosted, buried, filtered, or redirected, or whether certain queries are associated with other queries. See [Configure serving controls for search](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-serving-controls).

     * **Search-as-you-type.** If your app uses awkward input devices such as TV remote controls, you can enable the search-as-you-type feature. See [Get search-as-you-type results for a media app](https://docs.cloud.google.com/generative-ai-app-builder/docs/preview-search-results#media-search).




###  Filter and boost your search results

If you plan to deploy your app by integrating search API calls into your own code, you can configure filtering and boosting for your search results.

### Actions

  1. [Filter media search](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-media-search).

  2. [Boost search results](https://docs.cloud.google.com/generative-ai-app-builder/docs/boost-search-results).




###  Preview search results

You can preview your search results to check if your app configurations are working as expected.

### Actions

  1. To preview your search results, use the console or the API.

     * **Console.** Use the Agent Search console **Preview** page to preview how search widget configurations affect your results. See the **Console** instructions in [Get search results for media](https://docs.cloud.google.com/generative-ai-app-builder/docs/get-media-search-results).

     * **API**. If you're integrating API calls into your application, make API calls to preview your search configurations. See the **REST** instructions in [Get search results for media](https://docs.cloud.google.com/generative-ai-app-builder/docs/get-media-search-results).




###  Deploy your app

When you're happy with the preview version of your media search app, share it with your users by deploying it to your website.

### Actions

  1. You can deploy your search app in either of the following ways:

     * **Embed the search widget into your website.** Agent Search provides code that you can copy into your website or web application. This deploys the search widget. You can preview search results in the console. See [Add the search widget to a webpage](https://docs.cloud.google.com/generative-ai-app-builder/docs/add-widget).

     * **Integrate search API calls into your server or application.** For full control over how your search results are displayed, you can integrate API calls into your server or applications. For more information about making API calls, see [Get search results](https://docs.cloud.google.com/generative-ai-app-builder/docs/preview-search-results). For client library resources, see [Agent Search client libraries](https://docs.cloud.google.com/generative-ai-app-builder/docs/libraries).




###  Maintain your app

You can maintain your app to ensure that latest and necessary data is available in your data store.

### Actions

  1. [Refresh your structured data](https://docs.cloud.google.com/generative-ai-app-builder/docs/refresh-data#refresh-structured).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
