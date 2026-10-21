---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/healthcare-search-checklist/
title: Healthcare search checklist \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:27:59.996188+00:00
---

# Healthcare search checklist  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/healthcare-search-checklist/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Healthcare search checklist Stay organized with collections  Save and categorize content based on your preferences. 

Deprecated: Agent Search for healthcare is deprecated and won't be available after May 15, 2027. 

This page provides a checklist of the steps required to implement a healthcare search app. 

****

###  Set up a Google Cloud project

Set up a Google Cloud project, turn on Agent Search, and set up access control for your project. You can use an existing Google Cloud project if you have one already.

### Actions

  1. Review [Before you begin](https://docs.cloud.google.com/generative-ai-app-builder/docs/before-you-begin) and confirm that you have completed the steps.



###  Prepare your data

Prepare to import your source FHIR R4 data from a Cloud Healthcare API data store to your Agent Search data store.

### Actions

  1. Review the information about supported data and the relationship between healthcare search apps and data stores in [About apps and data stores](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-datastore-ingest).

  2. Prepare your source data according to the requirements in [Prepare data for ingestion](https://docs.cloud.google.com/generative-ai-app-builder/docs/prepare-data#hc-fhir-data).




###  Import your data

Create a data store and then import your data into it. You can perform a one-time batch import or set up a streaming import.

### Actions

  1. To create a data store and import data into it and later connect it to a healthcare search app, follow the instructions in [Create a healthcare search data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-hc).



###  Create your app

Create your healthcare search app and connect it to your new data store.

### Actions

  1. [Create a healthcare search app](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-app-hc).



###  Configure your search settings

Agent Search provides options to customize your search widget.

### Actions

Depending on your use case and whether you plan to deploy the out-of-the-box search widget or integrate search API calls into your own code, Agent Search provides several options for configuration.

  * **Search widget results.** Select the whether to perform a basic search or to search with an answer using LLMs. Applicable for a search widget. See [Configure results for the search widget](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-widget-attributes).

  * **Autocomplete.** Set up autocomplete suggestions to receive helpful query suggestions. See [Configure autocomplete](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-autocomplete).




###  Preview search results

Preview your search results to check if your app configurations are working as expected. You can search using keywords and natural language queries. You can also choose to get a generative AI answer.

### Actions

  1. Review the subset of FHIR resources, resource references, and elements that Agent Search supports. See [Healthcare FHIR R4 data schema reference](https://docs.cloud.google.com/generative-ai-app-builder/docs/fhir-schema-reference).

  2. Preview your search results, using the console or the API.

     * **Console.** Use the AI Applications console **Preview** page to preview how search widget configurations affect your results. See the **Console** instructions in [Search healthcare data](https://docs.cloud.google.com/generative-ai-app-builder/docs/search-hc-data).

     * **API**. If you're integrating API calls into your application, make API calls to preview your search configurations. See the **REST** instructions in [Search healthcare data](https://docs.cloud.google.com/generative-ai-app-builder/docs/search-hc-data).




###  Filter your search results

If you plan to deploy your app by integrating search API calls into your own code, Agent Search lets you customize the results.

### Actions

Configure your search requests with the following options:

  * **Filter results.** See [Filter healthcare search](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-hc-search).



###  Deploy your search app

When you are happy with the preview version of your search app, share it with your users by deploying it to your website.

### Actions

  1. You can deploy your search app in either of the following ways:

     * **Embed the search widget into your website.** Agent Search provides code that you can copy into your website or web application. This deploys the search widget. You can preview search results in the console. See [Add the search widget to a webpage](https://docs.cloud.google.com/generative-ai-app-builder/docs/add-widget).

     * **Integrate search API calls into your server or application.** For full control over how your search results are displayed, you can integrate API calls into your server or applications. For more information about making API calls, see [Search healthcare data](https://docs.cloud.google.com/generative-ai-app-builder/docs/search-hc-data). For client library resources, see [Agent Search client libraries](https://docs.cloud.google.com/generative-ai-app-builder/docs/libraries).




###  Maintain your app

You can maintain your app to ensure that latest and necessary data is available in your data store.

### Actions

  1. To refresh your data, see [Refresh healthcare data](https://docs.cloud.google.com/generative-ai-app-builder/docs/refresh-hc-data). Refresh your data only if you perform batch imports. You can skip this step if you have set up a streaming import.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
