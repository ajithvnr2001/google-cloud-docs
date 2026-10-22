---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/release-notes/
title: AI Commerce Search release notes \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:35:29.219825+00:00
---

# AI Commerce Search release notes  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  AI Commerce Search release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to AI Commerce Search. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/retail-release-notes.xml) directly. 

## June 29, 2026

Feature

Vertex AI Search for commerce, which has been previously known under the mame Retail Search, has been rebranded to AI Commerce Search in Gemini Enterprise for Customer Experience.

An intelligent AI search platform customized for ecommerce use cases, AI Commerce Search now belongs to the Gemini Enterprise for Customer Experience product suite.

For general product information, see [AI Commerce Search on Gemini Enterprise for Customer Experience](https://cloud.google.com/gemini-enterprise-cx/commerce?e=48754805).

## November 14, 2025

Feature

The Vertex AI Search for commerce Merchandising console introduces self-serve and agentic explainability for issue diagnosis. Streamlined governance is supported with distinct Creator and Approver roles. New features enhance preview and provide real-time control application feedback.

For more information, see [Serving controls in the Merchandising console](https://cloud.google.com/gemini-enterprise-cx/ai-commerce-search/merchandising-controls).

## September 15, 2025

Feature

**Vertex AI Search for commerce: Additional languages added to search (GA)**

Additional languages, including Urdu and Serbian (Cyrillic), are supported in Vertex AI Search for commerce. 

For a list of the languages supported, see [Supported world languages](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/supported-languages#search-languages).

## September 05, 2025

Feature

**Vertex AI Search for commerce: Conversational product filtering**

As part of Search for commerce's Guided search package, `ConversationalSearchSpec` sits on top of the Vertex AI Search for commerce. When coverage parameters are met, Search for commerce users can enable this feature in the console or by setting the `followup_conversation_requested` flag to `true` in the search service interface. Conversational product filtering uses an LLM-generated question for each catalog attribute where `allowed_in_conversation` field is enabled.

For more information, see [Conversational product filtering](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/conversational-filtering).

## September 03, 2025

Feature

**Vertex AI Search for commerce: Conversational Commerce agent, GA**

The Conversational Commerce agent uses LLM and conversational product filtering to provide users with a real-time, ongoing conversational experience. The conversational product filtering feature functions as part of the Guided Search package, helping narrow down search queries sooner by presenting users with either relevant products, follow-up questions, or both.

The Conversational Commerce agent is generally available (GA). For information, see [Conversational Commerce agent](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/conversational-search) and [Conversational product filtering](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/conversational-filtering).

## March 11, 2025

Feature

**Vertex AI Search for commerce: Conversational Commerce agent, private preview**

The Conversational Commerce agent uses LLM and conversational product filtering to provide users with a real-time, ongoing conversational experience. The conversational product filtering feature functions as part of the Guided Search package, helping narrow down search queries sooner by presenting users with either relevant products, follow-up questions, or both.

The Conversational Commerce agent is in private preview. For more information, see [Conversational Commerce agent](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/conversational-search) and [Conversational product filtering](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/conversational-filtering).

## February 03, 2025

Feature

Pinning is available for Vertex AI Search for commerce. Pinning is a serving control for that lets you specify an exact position in search results for a certain item to appear.

The pinning control is created by adding a rule to the search or browse condition, which is the action field `pin_action` in the Retail API. A pin value from 1 to 120 can be applied to determine the fixed position for results matching the defined conditions. This feature is not supported for recommendations.

For more about pinning, see [Pinning controls](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/serving-control-rules#pinning).

## January 31, 2025

Feature

**Vertex AI Search for commerce: Merchandising console**

Vertex AI Search for commerce has released a new user-friendly Merchandising console for site merchants and business users. Cloud console admins can grant users access as a Creator or Approver to set or define rules, and create and manage controls. The Google Cloud Search for commerce console Controls section has a Merchandising console tab where admins can grant users access and manage user permissions for the Merchandising console.

For more information, see [Console options for creating controls](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-controls#console-options).

## January 10, 2025

Change

**Vertex AI Search for commerce: Renamed in the console and documentation**

Vertex AI Search for retail is renamed as Vertex AI Search for commerce. The Google Cloud console and the documentation at cloud.google.com have been updated to reflect the rename. In the console, look for **Search for Commerce**.

## September 27, 2024

Feature

**Vertex AI Search for retail: Tile navigation**

As part of Search for retail's Guided search package, tile navigation allows tiles to appear for each of the most likely to be used dynamic facets across a search page. The objective is to increase filter usage to narrow search faster.

For more information, see [Tile navigation](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/tiles).

Feature

**Vertex AI Search for retail: Conversational search API**

As part of Search for retail's Guided search package, `ConversationalSearchSpec` sits on top of the Retail API. When coverage parameters are met, Search for retail users can enable this feature in the console or by setting the `followup_conversation_requested` flag to `true` in the search service interface. Conversational search uses an LLM-generated question for each catalog attribute where `allowed_in_conversation` field is enabled.

For more information, see [Conversational search](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/conversational-search).

## March 29, 2024

Feature

**Vertex AI Retail Search: Search analytics v2 improvements**

  * Enhanced dashboard experience: Leverages Looker for a more interactive and informative analysis of your search and browse performance.
  * Detailed metrics: Gain granular insights with per-search/per-browse metrics, along with metrics tied to search/browse visits.
  * Full funnel reporting: Analyze page-views, add-to-cart events, purchases, and revenue to understand the entire customer conversion journey.
  * Flexible analysis: Filter data by date ranges and device types to tailor your analysis.



## March 12, 2024

Change

**Vertex AI Search for retail: Renamed in the console and documentation**

The Google Cloud console has been updated to show the current product name for Vertex AI Search for retail.

You might see the old names (Retail or Retail API) in some places—for example, in the documentation. Google is in the process of updating content to reflect the new branding.

## December 15, 2023

Change

**Retail API: Export analytics metrics to BigQuery**

You can export Retail analytics metrics into BigQuery. Exporting analytics metrics allows you to retain metrics and write SQL for your own analysis.

For more information, see [Export your analytics metrics into BigQuery](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/export-analytics-metrics).

## December 12, 2023

Feature

**Retail Search: Retail Search with LLM public preview**

Retail Search with LLM is in public preview.

Retail Search with LLM improves ranking by improving AI-driven grading of how relevant each product is for a specific query. 

Prior to this upgrade, these relevance grades were generated by an older generation of AI that produced imperfect scoring. This sometimes caused low-relevance products to be highly ranked in search results.

With this upgrade, Retail Search uses state-of-the-art AI techniques to do the following:

  * Develop a Giant Relevance LLM that can accurately grade product/query relevance in any retail category in any supported language.
  * Distill a smaller LLM that is specific to one retailer from the Giant Relevance LLM. This smaller LLM contains the knowledge needed to grade query/product relevance for a specific retailer's catalog and their unique query stream.
  * Use the smaller, retail-specific LLM to accurately grade products in real-time.
  * Allow downstream AIs in Retail Search that consume these more accurate query/product relevance grades to correctly rank lower-relevance products as lower in search results.
  * Lead to increases in revenues and visits for retailers by focusing early search results on higher-relevance products.



_Who has access to Retail Search with LLM in the public preview phase?_

You must meet the access criteria to be considered for the Public Preview. You need to have:

  * A fully onboarded Retail project. This means the project is: 
    * Fully onboarded onto Retail Search
    * Has stable usage. It is being used for production, has no sudden ramps up/down, and has no off-label (unsupported) usage
    * Correctly onboarded with no major data quality issues
  * Sufficient search volumes: 
    * Have >5M searches/day (counting search only, no browse) served by Retail Search for each of the past 30 days



If you have multiple projects, you can choose only one project to use for the public preview.

## November 02, 2023

Feature

**Retail API: Configure logging**

You can configure which service logs are written to Cloud Logging. Logging configuration provides a way to set the severity levels at which to write logs, turn logging on or off, and override default logging settings for specific services. For information on how to change Logging configurations, see [Configure Logging](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/error-reporting#log-config).

## October 03, 2023

Feature

**Retail Search: Facet controls**

You can create facet controls that apply to search and browse operations. These help you control facets values without editing your catalog and set the ranking of facet keys. 

Numerical facets have been improved: intervals are calculated but they can also be customized.

The facet controls are:

  * Ignore facet values
  * Replace facet values
  * Set numerical intervals
  * Remove facets
  * Force return facets



For more information, see [Facets for search](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/facets-overview).

## August 04, 2023

Feature

**Retail API: View search performance tiers and performance upgrade requirements**

Text query search and browse search have different performance tiers that increasingly improve your search results. Unlocking performance tiers relies on the user event and catalog data that you upload to Retail. The Retail console provides a **Data Quality** page where you can check if you have met each tier's data requirements.

For documentation about search performance tiers and how to check data requirements, see [Unlock search performance tiers](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/data-quality).

## June 26, 2023

Announcement

**Retail API: Data export for analytics and other use cases is in GA**

Exporting retail data into BigQuery is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)), allowing you to extract insights from your data. You can use the data to get Key Performance Indicators with our out-of-the-box [Looker dashboard](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/get-dashboards-that-show-kpis), and sales forecasts using [Vertex AI](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/generate-sales-forecasts) and our step-by-step instructions.

Feature

The **Data quality** page assesses the quality of your product catalog and user event data and shows you which search performance tiers you have unlocked for Retail Search. 

For more information, see [Unlock search performance tiers](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/data-quality). 

The **Data quality** _page_ replaces the **Data Quality** _panel_ which was on the Retail console Data page.

Feature

**Entities** are available as a way to subdivide your retail organization into more than one segment. For example, entities can represent different regions where stores are located or differently branded stores, such as acquisitions. Recommendations, search results, and autocomplete can give results tailored specifically for an entity. 

For more information, see [Entities](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/entities).

## February 06, 2023

Feature

Retail Search catalog support for Korean, Polish, and Turkish is now generally available (GA). For a list of all languages supported by the Retail Search catalog, see the [FAQ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/faq#catalogs_and_products).

## January 12, 2023

Feature

Browse search is generally available using Retail Search. Typically, browsing products using site navigation produces results that are all of equal relevance or sorted by best-selling items. Retail Search leverages AI to optimize how browse results are sorted by considering popularity, buyability, and personalization. See [About text search and browse search with Retail Search](https://cloud.google.com/gemini-enterprise-cx/ai-commerce-search/search-basic#about_text_search_and_browse_search_with).

Feature

Retail Search can now automatically deliver personalized results for your text query searches and browse searches. Results are personalized for each end-user based on their behavior on your site, including each user's history of product views, clicks, additions to carts, and purchases.

You can use the Data Quality panel on the Retail console Data page to get an assessment of whether the data you have imported is sufficient to turn on automatic personalization. See [Personalization](https://cloud.google.com/gemini-enterprise-cx/ai-commerce-search/search-basic#personalization).

Feature

The Page-level Optimization model is now generally available. Page-level Optimization extends Recommendations AI from optimizing for a single recommendation panel at a time to optimizing for an entire page with multiple panels. The Page-level Optimization model selects the contents for each panel and determines the panel order on your page. For more about this feature, see [Page-level Optimization](https://cloud.google.com/gemini-enterprise-cx/ai-commerce-search/models#plo).

## December 22, 2022

Feature

Recommendations AI now provides the On-sale model. The On-sale model is a personalized promotions-based model that can recommend on-sale products. You can use this model type to encourage users to purchase discounted items.

For more information about the On-sale model, see the [About recommendation models](https://cloud.google.com/gemini-enterprise-cx/ai-commerce-search/models) documentation. For how to create this model, see [Create recommendation models](https://cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-models).

## October 27, 2022

Feature

Recording Google Analytics 4 user events to the Retail API is available in GA. If you have integrated Google Analytics 4 for your user events, you can record the user event data in Google Analytics 4 format directly to the Retail API.

To use this feature, see the [Record user events with Google Analytics 4](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/record-events) documentation.

Feature

A/B experiment traffic monitoring for Retail Search is available in private preview. See the documentation for [A/B experiment monitoring](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/a-b-monitor).

A/B experiments compare key metrics between the Retail API and your existing search implementation. After setting up an experiment and its traffic splitting, you can monitor experiment traffic using the Retail console. In the console, you create variant arms that map to each experiment group that you created for the A/B experiment. This allows you to check whether the actual traffic matches the intended traffic split of your experiment. Traffic monitoring can help you determine if differences in traffic are due to a quality gap between services or an incorrect experiment setup.

To use A/B experiment traffic monitoring in private preview, contact Retail Support.

## October 12, 2022

Feature

Recommendations AI now provides two diversification options when you create serving configs for recommendations.

  * Ruled-based diversification affects whether results returned from a single prediction request are from different categories of your product catalog.
  * Data-driven diversification uses machine learning to balance category diversity and relevance in your prediction results.



For more about diversification types, see the [Diversification](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/configs#diversification) documentation.

Feature

Auto-completion for Retail Search is now GA. 

Auto-completion predicts the rest of a query a user is typing, which can improve the user search experience and accelerate the shopping process before checkout.

For more about auto-completion for Retail Search, see the [Auto-completion documentation](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/completion-overview).

Feature

Recommendations AI now provides a revenue per session optimization objective for the Others You May Like and Frequently Bought Together model types.

This objective works differently for each model type, but always optimizes for revenue by recommending items that have a higher probability of being added to carts.

For more about the revenue per session optimization objective, see the [Revenue per session](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/models#rps) documentation.

Feature

Recommendations AI now provides a Buy It Again model.

The Buy it Again model encourages purchasing items again based on previous recurring purchases.This personalized model predicts products that have been previously bought at least once and that are typically bought on a regular cadence.

For more information about the Buy It Again model, see the [Buy It Again documentation](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/models#bia). For how to create this model, see [Create models](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-models).

## September 27, 2022

Change

The **Monitoring & Analytics** page has been split into two separate pages. The contents of the old **Monitoring** _tab_ appear on the new **Monitoring** _page_ , and the contents for the old **Analytics** _tab_ appear on the new **Analytics** _page_.

## September 23, 2022

Feature

Recommendations AI now provides a Page-Level Optimization model. This extends Recommendations AI from optimizing for a single recommendation panel at a time to optimizing for an entire page with multiple panels. When creating a Page-Level Optimization model, you specify existing serving configurations that this model can use as candidates for each recommendation panel. Page-Level Optimization model then automates the decision process for coordinating model combinations and layouts by automatically selecting the contents for each panel and determining the panel order on your page. 

For more information about the Page-Level Optimization model, see the [Page-Level Optimization documentation](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/models#plo). For how to create this model, see [Create models](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-models).

## September 15, 2022

Feature

Bulk importing of historical Google Analytics 4 user events with BigQuery is generally available. You can use this feature to import user events to the Retail API if you have integrated Google Analytics 4 with BigQuery and use Enhanced Ecommerce. 

See the new documentation: [Import Google Analytics 4 user events with BigQuery](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/import-user-events#bq-ga4)

## August 03, 2022

Feature

Serving controls can now be imported from and exported to files. This allows you to move serving controls between projects and do bulk edits and additions of serving controls within a project. This feature is available in Preview.

See the new documentation:

  * [Export serving controls](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/manage-controls#export)
  * [Import serving controls](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/manage-controls#import)



## April 05, 2022

Feature

Retail Search is generally available.

For available features, see [Features and capabilities](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/features#retail-search). 

For an overview of the steps to take to implement Retail Search, see [Implementing the Retail API](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/overview). To begin setting up Retail Search, go to [Before you begin](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/setting-up).

Change

There are new data use terms for access and use of customer data for Recommendations AI and Retail Search. To view them, go to [Terms for data use](https://docs.cloud.google.com/retail/data-use-terms).

The new terms will be rolled out to Cloud Console from April 4 to 8, 2022. You will be required to accept these terms within 90 days to continue using Retail solutions uninterrupted.

To accept the data use terms:

  1. Access the Cloud Console and select your projects using Recommendations AI and/or Retail Search.
  2. The data use terms will appear on this page. If you wish to continue using our Retail solutions, please accept the terms for all projects using Recommendations AI and/or Retail Search.



If you wish to reject the terms, please disable all projects using the Cloud Retail API (Recommendations AI and Retail Search) in the Cloud Console.

We strongly encourage you to accept the terms before July 13, 2022. If you haven't accepted the terms by this date, you will lose API functionality.

For more details, please review our data use practices at [Retail API data use](https://docs.cloud.google.com/retail/data-use).

## January 21, 2022

Feature

The Retail console is now available to all Recommendations AI users. The Retail Console is a new way to manage both Recommendations AI and Retail Search seamlessly in one project through a unified onboarding and admin console experience.

We recommend [switching to the Retail console](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/console-migration) and [using the Retail documentation](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/how-to), which documents Recommendations AI, the Retail console, and Retail Search. 

To switch, go to the new console and click **Enable the Retail API**. You can then view and manage your project from the new console.

## January 15, 2021

Announcement

Recommendations AI is now generally available.

This product has migrated to the Retail API from the Recommendations Engine API.

The previous API (service endpoint `https://recommendationengine.googleapis.com`) and its [documentation set](https://docs.cloud.google.com/recommendations-ai/docs/apis) remain available, but they will no longer be updated. If you used the previous API while it was in beta, we recommend migrating your recommendations to the Retail API (service endpoint `https://retail.googleapis.com`). 

See the new documentation:

  * [How-to documentation for Recommendations AI](https://docs.cloud.google.com/retail/recommendations-ai/docs/how-to)
  * [Reference documentation for the Retail API](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/apis)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
