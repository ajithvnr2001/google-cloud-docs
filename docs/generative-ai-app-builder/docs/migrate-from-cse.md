---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/migrate-from-cse/
title: Migrate from Custom Search Site Restricted JSON API \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:28:05.130549+00:00
---

# Migrate from Custom Search Site Restricted JSON API  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/migrate-from-cse/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Migrate from Custom Search Site Restricted JSON API Stay organized with collections  Save and categorize content based on your preferences. 

If you use the [Custom Search Site Restricted JSON API](https://developers.google.com/custom-search/v1/site_restricted_api) of Programmable Search Engine, you can create and deploy Google-quality, site-restricted search in minutes, using Agent Search. To deploy your app, you can use the [search widget](https://docs.cloud.google.com/generative-ai-app-builder/docs/add-widget) by copying code from the Google Cloud console directly into a web page—no coding required. Or, you can implement an API deployment to have control over how search functionality looks on your website. For more information about using the API, see the REST tab of [Get search results for an app with website data](https://docs.cloud.google.com/generative-ai-app-builder/docs/preview-search-results#web) and the [`servingConfigs.search`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/search) method in the REST reference.

In addition to the standard short snippets that Agent Search returns with search results, you can add advanced features to your search. These include generated [summaries](https://docs.cloud.google.com/generative-ai-app-builder/docs/get-search-summaries) of search results, [search with follow-ups](https://docs.cloud.google.com/generative-ai-app-builder/docs/answer#commands_for_follow-up_questions) for context-aware search that allows follow-up questions, and [extractive answers](https://docs.cloud.google.com/generative-ai-app-builder/docs/snippets#extractive-answers) for extracted text returned with each search result. Getting these advanced features for your web search requires [domain verification](https://docs.cloud.google.com/generative-ai-app-builder/docs/domain-verification) and incurs additional indexing costs.

You can also [filter](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-website-search#filter-expressions-basic-indexing) or [order](https://docs.cloud.google.com/generative-ai-app-builder/docs/order-web-search-results#basic-indexing) your search results and apply [promote controls](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-serving-controls#promote) to display a link as a promoted result.

For more information, see the [Agent Search pricing](https://docs.cloud.google.com/generative-ai-app-builder/pricing) page.

## Set up Agent Search

To set up Agent Search, follow these steps:

  1. In the Google Cloud console, on the [project selector page](https://console.cloud.google.com/projectselector2/home/dashboard), select the project that you've been using for the Custom Search Site Restricted JSON API.

  2. [Turn on Agent Search](https://docs.cloud.google.com/generative-ai-app-builder/docs/before-you-begin#turn-on-discovery-engine).




## Create a search app

To create a search app, follow these steps:

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/engines)

  2. Click **Create app**.

  3. On the **Create App** page, under **Site search with AI mode** , click **Create**.

  4. Make sure **Enterprise edition features** is turned on. This is required for website search. For more information, see [Enterprise edition features](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-advanced-features#enterprise-features).

  5. Turn off **Generative Responses**. Turning this off gives you functionality similar to the Custom Search Site Restricted JSON API of Programmable Search Engine. Turn this off if you don't need search summarization or search with follow-ups. For more information, see [Generative responses](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-advanced-features#generative-response-features).

  6. In the **Your app name** field, enter a name for your app.

  7. In the **External name of your company or organization** field, enter the common name for your company or organization.

  8. Select **global (Global)** as the location for your app, and then click **Continue**.

  9. On the **Data Stores** page, click **Create data store**.

  10. In the **Select a data source** pane, select **Website Content**.

  11. Turn off **Advanced website indexing** indexing. Turning this off gives you functionality similar to the Custom Search Site Restricted JSON API of Programmable Search Engine. Turn this off if you don't need search summarization or search with follow-ups, or if you don't own the domains that you specify. For more information, see [Advanced website indexing](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-advanced-features#advanced-website-indexing).

  12. In the **Specify URL patterns to index** pane, in the **Sites to include** field, enter the URL patterns of the websites that you want to search, and then click **Continue**.

  13. In the **Configure your data store** pane, enter a display name for your data store, and then click **Create**.

  14. On the **Data Stores** page, select your new data store, and then click **Create**.




## Deploy the search app

Decide how you plan to authenticate your Agent Search search app: using OAuth 2.0 or an API key. For information about the advantages and disadvantages of each method, see About authentication.

  * To deploy the search app with OAuth 2.0

  * To deploy the search app with an API key




### Deploy the search app (OAuth 2.0)

To deploy your search app using OAuth 2.0 authentication, follow these steps:

  1. To set up OAuth 2.0, see [On Google Cloud](https://docs.cloud.google.com/generative-ai-app-builder/docs/authentication#on-gcp) in _Authenticate to Agent Search_. Make sure to add the [Discovery Engine User](https://docs.cloud.google.com/generative-ai-app-builder/docs/access-control#discoveryengine.user) or the [Discovery Engine Viewer](https://docs.cloud.google.com/generative-ai-app-builder/docs/access-control#discoveryengine.viewer) role to the service account.

  2. Deploy your search app in one of the following ways:

     * **Use the search widget.** Deploy your search app with no coding required. For more information, see [Add the search widget to a web page](https://docs.cloud.google.com/generative-ai-app-builder/docs/add-widget).

     * **Use the API.** Use the API to control how search functionality looks on your website. For more information, see the REST tab of [Get search results for an app with website data](https://docs.cloud.google.com/generative-ai-app-builder/docs/preview-search-results#web) and the [`servingConfigs.search`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/search) method in the REST reference. To order the results of your web search queries, see [Order web search results](https://docs.cloud.google.com/generative-ai-app-builder/docs/order-web-search-results).




### Deploy the search app (API key)

To deploy your search app using an API key for authentication, follow these steps:

  1. Create the API key:

     1. In the Google Cloud console, go to the **Credentials** page.

[Credentials](https://console.cloud.google.com/apis/credentials)

     2. If you're not already in your project, in the project list at the top of the Google Cloud console page, select your project.

     3. Click **Create credentials** and then select **API key**. _Don't add any referrer restrictions_. Some user privacy settings don't pass the referrer URL.

        * Take note of the generated API key, which you will use when calling the `searchLite` method.
     4. For increased security, add an [HTTP restriction](https://docs.cloud.google.com/docs/authentication/api-keys#api_key_restrictions) to your API Key to restrict access to the Agent Search service at `https://discoveryengine.googleapis.com/*`.

  2. Deploy your search app using the API. See [Get search results for an app with website data (API key)](https://docs.cloud.google.com/generative-ai-app-builder/docs/preview-search-results#web-api-key) and the [`servingConfigs.searchLite`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/searchLite) method in the REST reference. To order the results of your web search queries, see [Order web search results](https://docs.cloud.google.com/generative-ai-app-builder/docs/order-web-search-results).




## About authentication

The [Custom Search Site Restricted JSON API](https://developers.google.com/custom-search/v1/site_restricted_api) of Programmable Search Engine authenticates using an API key. While, with a couple of exceptions, Agent Search requires OAuth 2.0. If you want to carry on using an API key for authentication, then you need to use the [`searchLite`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines.servingConfigs/searchLite) method through API calls.

If you choose to authenticate through OAuth 2.0, then you need to use the [`search`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.servingConfigs/search) method and the [`answer`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.servingConfigs/answer) method to query your website, furthermore, you can deploy your search app through the no-code search widget.

The following table lists differences between using the `searchLite` method with API key authentication and the `search` and `answer` methods with OAuth 2.0 authentication.

Feature/Methods | `searchLite` method | `search` method  
---|---|---  
**Authentication** | API key | OAuth 2.0  
**Search widget available** | ✘ | ✔  
**Search summaries** | ✔ | ✔  
**Search public websites** | ✔ | ✔  
  
## Next steps

  * If you need to filter the search results, see [Filter expressions for basic website search](https://docs.cloud.google.com/generative-ai-app-builder/docs/filter-website-search#filter-expressions-basic-indexing).

  * If you need to provide image search, see [Search for images on websites](https://docs.cloud.google.com/generative-ai-app-builder/docs/image-search).

  * If you need to order the search results, for example by date, see [Order search results for basic website search](https://docs.cloud.google.com/generative-ai-app-builder/docs/order-web-search-results#basic-indexing).

  * If you need multi-turn search, see [Commands for follow-up questions](https://docs.cloud.google.com/generative-ai-app-builder/docs/answer#commands_for_follow-up_questions).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
