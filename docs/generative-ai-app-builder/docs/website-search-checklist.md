---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/website-search-checklist/
title: Website search checklist \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:43.729167+00:00
---

# Website search checklist  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/website-search-checklist/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Website search checklist Stay organized with collections  Save and categorize content based on your preferences. 

This page provides a checklist of the steps required to create a website search app, which is a type of custom search app. For a checklist to create other types of custom search apps, see [Custom search checklist](https://docs.cloud.google.com/generative-ai-app-builder/docs/generic-search-checklist). 

If you're new to Agent Search, consider following the [Get started with custom search](https://docs.cloud.google.com/generative-ai-app-builder/docs/try-enterprise-search) tutorial to create a sample website data app.

## Choose between basic website search and advanced website indexing

Agent Search offers two types of website data stores: basic website search and advanced website indexing.

You can choose to turn on advanced website indexing to index the web pages in your search data store. Advanced website indexing requires domain verification and offers several additional features over basic website search. For more information, see [Advanced website indexing](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-advanced-features#advanced-website-indexing).

Depending on the type of website data store you require for your business needs, select one of the following checklists:

Basic website search Advanced website indexing

****

###  Set up a Google Cloud project

Set up a Google Cloud project, turn on Agent Search, and set up access control for your project. You can use an existing Google Cloud project if you already have one.

### Actions

  1. Review the [Before you begin](https://docs.cloud.google.com/generative-ai-app-builder/docs/before-you-begin) page and confirm that you have completed the steps.



###  Prepare your data

Understand how a website search app (a type of custom search app) behaves and the prerequisites to include websites in a website data store.

### Actions

  1. Review the information about the relationship between custom apps and data stores in [About apps and data stores](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-datastore-ingest#app-store-relationship) and what constitutes [website data](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-datastore-ingest#websites). For basic website search, you can connect only one data store to an app.

  2. Prepare your website data according to the requirements in [Website data](https://docs.cloud.google.com/generative-ai-app-builder/docs/prepare-data#website).




###  Create a data store

Create a data store by providing the website URL patterns to include and the URL patterns to exclude.

### Actions

  1. Follow the instructions for your data source in [Create a data store using website URLs](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es#website).



###  Create your app

Create your website search app and connect it to your new data store.

### Actions

  1. [Create a search app](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-engine-es). Ensure to turn on enterprise edition.



###  Set up billing

Agent Search for custom search supports two pricing models:

  * **General** : A pay-as-you-go consumption-based model.
  * **Configurable** : A mixed-pricing model that lets you to unbundle capabilities and create a subscription package that is more closely aligned with your specific use cases. This pricing model lets you to pay only for the features that you need and benefit from their powerful capabilities. It offers two subscriptions and optional add-ons. After you enable this pricing model at project level, you can select configurable pricing for your apps and data stores.



### Actions

By default, a project is set to the pay-as-you-go model. However, to switch to the configurable pricing, do the following:

  1. Follow the instructions to [Set up configurable pricing for custom search](https://docs.cloud.google.com/generative-ai-app-builder/docs/enable-configurable-pricing). Don't select any add-ons and set the **Storage Subscription Threshold** to the minimum. (Basic web apps don't use storage.)



###  Configure your search settings at a data store level

Agent Search provides many configuration options. Some options depend on whether you plan to deploy a search widget.

### Actions

Depending on your use case and whether you plan to deploy the out-of-the-box search widget or integrate search API calls into your own code, Agent Search provides several options for configuration.

  * You can embed a search widget into your website. The widget automatically provides a search bar and expandable search interface. If you plan to deploy the search widget, configure the following:

    * **Search widget results.** See [Configure results for the search widget](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-widget-attributes).

    * **Autocomplete.** See [Update autocomplete settings](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-autocomplete#update_autocomplete_settings).

  * If you plan to integrate search API calls into your server or application instead of using the widget, you can configure your search settings using the following options:

    * **Autocomplete.** Depending on your data, set up autocomplete suggestions based on document content, fields, search history, or user events. See [Configure autocomplete](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-autocomplete).

    * **Serving controls.** Control when search results are filtered or promoted. See [Configure serving controls for search](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-serving-controls).




###  Configure your search results at a request level

If you plan to deploy your app by integrating search API calls into your own code, Agent Search provides additional options for configuring how your search results are returned.

### Actions

  1. Configure your search results with the following options:

     * [Filter website search](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-website-search) using filter expressions for basic website search.
     * [Order web search results](https://docs.cloud.google.com/generative-ai-app-builder/docs/order-web-search-results) for basic website search.
     * [Get snippets](https://docs.cloud.google.com/generative-ai-app-builder/docs/snippets).



###  Preview search results

You can preview your search results to check if your app configurations are working as expected.

### Actions

  1. To preview your search results, use the console or the API.

     * **Console.** Use the Agent Search console **Preview** page to preview how search widget configurations affect your results. See the **Console** instructions in [Get search results](https://docs.cloud.google.com/generative-ai-app-builder/docs/preview-search-results).

     * **API**. If you're integrating API calls into your application, you can make cURL calls to preview your search configurations. See the **REST** instructions in [Get search results](https://docs.cloud.google.com/generative-ai-app-builder/docs/preview-search-results).




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



###  Turn on advanced website indexing

You can upgrade your search app to advanced website indexing at any time. Advanced website indexing offers [features](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-advanced-features#advanced-website-indexing) that enrich your indexing to enhance your search experience.

### Actions

  1. [Turn on advanced website indexing](https://docs.cloud.google.com/generative-ai-app-builder/docs/turn-on-advanced-indexing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
