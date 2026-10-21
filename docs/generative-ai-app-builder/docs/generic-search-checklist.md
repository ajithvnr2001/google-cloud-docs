---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/generic-search-checklist/
title: Custom search checklist \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:27:59.214890+00:00
---

# Custom search checklist  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/generic-search-checklist/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Custom search checklist Stay organized with collections  Save and categorize content based on your preferences. 

This page provides a checklist of the steps required to create a custom search app. For a checklist to create a website search app, see [Website search checklist](https://docs.cloud.google.com/generative-ai-app-builder/docs/website-search-checklist). 

If you're new to Agent Search, consider following the [Get started with custom search](https://docs.cloud.google.com/generative-ai-app-builder/docs/try-enterprise-search) tutorial to create a sample app. 

****

###  Set up a Google Cloud project

Set up a Google Cloud project, turn on Agent Search, and set up access control for your project. You can use an existing Google Cloud project if you have one already.

### Actions

  1. Review [Before you begin](https://docs.cloud.google.com/generative-ai-app-builder/docs/before-you-begin) and confirm that you have completed the steps.



###  Prepare your data

Determine what kind of data you'll make available in your search app and prepare it for importing to Agent Search.

You can base your data store on the following types of data:

  * **Unstructured data.** Documents (such as PDFs, HTML files, and TXT files) that are stored in Cloud Storage. Optionally, you can provide metadata in a JSON file or in a BigQuery table.
  * **Structured data.** Data provided with a specific schema. For example, you can provide data in a BigQuery table, as JSON files in Cloud Storage, or from third-party connectors such as Jira.



### Actions

  1. Review the information about supported data and the relationship between apps and data stores in [About apps and data stores](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-datastore-ingest).

  2. Prepare your data according to the requirements in [Prepare data for ingestion](https://docs.cloud.google.com/generative-ai-app-builder/docs/prepare-data).

  3. If you need to set up access control to limit the data that users can view in your search app's results, review the prerequisites and follow the instructions for your identity provider type and data source in [Use data source access control](https://docs.cloud.google.com/generative-ai-app-builder/docs/data-source-access-control).




###  Import your data

Create a data store and then import your data into it, or set up a third-party connector as your synced data source.

How you import your data depends on where you're importing it from. For example, if your data is in Cloud Storage, you can import it using the console or the API by providing the bucket location of your data.

### Actions

  1. Follow the instructions for your data source in [Create a search data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es).



###  Create your app

Create your custom search app and connect it to your new data store.

### Actions

  1. [Create a search app](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-engine-es).



###  Set up billing

Agent Search for custom search supports two pricing models:

  * **General** : A pay-as-you-go consumption-based model.
  * **Configurable** : A mixed-pricing model that lets you to unbundle capabilities and create a subscription package that is more closely aligned with your specific use cases. This pricing model lets you to pay only for the features that you need and benefit from their powerful capabilities. It offers two subscriptions and optional add-ons. After you enable this pricing model at project level, you can select configurable pricing for your apps and data stores.



### Actions

By default, a project is set to the pay-as-you-go model. However, to switch to the configurable pricing, do the following:

  1. Follow the instructions to [Set up configurable pricing for custom search](https://docs.cloud.google.com/generative-ai-app-builder/docs/enable-configurable-pricing).



###  Configure your search settings

Agent Search provides many configuration options. Some options depend on whether you plan to deploy a search widget.

### Actions

Depending on your use case and whether you plan to deploy the out-of-the-box search widget or integrate search API calls into your own code, Agent Search provides several options for configuration.

  1. You can embed a search widget into your website. The widget automatically provides a search bar and expandable search interface. If you plan to deploy the search widget, configure the following:

     * **Search widget results.** See [Configure results for the search widget](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-widget-attributes).

     * **Search widget facets (Preview).** See [Configure facets for the search widget](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-widget-facets).

  2. If you plan to integrate search API calls into your server or application instead of using the widget, you can configure your search settings using the following options:

     * **Field settings.** For structured data or for unstructured data with metadata, update field settings to refine how Agent Search uses metadata for search. See [Configure fields for search](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-search-attributes).

     * **Autocomplete.** Depending on your data, set up autocomplete suggestions based on document content, fields, search history, or user events. See [Configure autocomplete](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-autocomplete).

     * **Serving controls.** Control when search results are boosted, buried, filtered, or redirected, or whether certain queries are associated with other queries. See [Configure serving controls](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-serving-controls).

     * **Search tuning (Preview).** Tune the search model with your own training data. See [Improve search results with search tuning](https://docs.cloud.google.com/generative-ai-app-builder/docs/tune-search).

     * **Custom embeddings (Preview).** If you've created your own embeddings, you might prefer to use them instead of those generated by Agent Search to enrich your searches with additional context. This feature is available for data stores with structured data or unstructured data with metadata. See [Use custom embeddings](https://docs.cloud.google.com/generative-ai-app-builder/docs/bring-embeddings).




###  Configure your search results

If you plan to deploy your app by integrating search API calls into your own code, Agent Search provides additional options for configuring how your search results are returned.

### Actions

  1. Configure your search results with the following options:

     * [Filter custom search for structured or unstructured data](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata).
     * **Get snippets, extractive answers, or extractive segments.** See [Get snippets and extracted content](https://docs.cloud.google.com/generative-ai-app-builder/docs/snippets).



###  Preview search results

You can preview your search results to check if your app configurations are working as expected.

### Actions

  1. To preview your search results, use the console or the API.

     * **Console.** Use the Agent Search console **Preview** page to preview how search widget configurations affect your results. See the **Console** instructions in [Get search results](https://docs.cloud.google.com/generative-ai-app-builder/docs/preview-search-results).

     * **API**. If you're integrating API calls into your application, make API calls to preview your search configurations. See the **REST** instructions in [Get search results](https://docs.cloud.google.com/generative-ai-app-builder/docs/preview-search-results).




###  Deploy your search app

When you're happy with the preview version of your search app, share it with your users by deploying it to your website.

### Actions

  1. You can deploy your search app in either of the following ways:

     * **Embed the search widget into your website.** Agent Search provides code that you can copy into your website or web application. This deploys the search widget. You can preview search results in the console. See [Add the search widget to a webpage](https://docs.cloud.google.com/generative-ai-app-builder/docs/add-widget).

     * **Integrate search API calls into your server or application.** For full control over how your search results are displayed, you can integrate API calls into your server or applications. For more information about making API calls, see [Get search results](https://docs.cloud.google.com/generative-ai-app-builder/docs/preview-search-results). For client library resources, see [Agent Search client libraries](https://docs.cloud.google.com/generative-ai-app-builder/docs/libraries).




###  Record and import user events

To get personalized search and browse results, you can update the user events in your search app. For more information see [About user events for custom apps](https://docs.cloud.google.com/generative-ai-app-builder/docs/user-events).

### Actions

  1. [Import historical user events](https://docs.cloud.google.com/generative-ai-app-builder/docs/import-user-events).
  2. [Record real-time user events](https://docs.cloud.google.com/generative-ai-app-builder/docs/record-user-events).



###  Maintain your app

You can maintain your app to ensure that latest and necessary data is available in your data store.

### Actions

  1. [Refresh your data](https://docs.cloud.google.com/generative-ai-app-builder/docs/refresh-data).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
