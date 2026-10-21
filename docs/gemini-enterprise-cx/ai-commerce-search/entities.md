---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/entities/
title: Entities \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:38:58.367657+00:00
---

# Entities  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/entities/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Entities Stay organized with collections  Save and categorize content based on your preferences. 

This page introduces _entities_ , ways of capturing varied user behavior depending on multiple brands or products on a single enterprise site, as well as how and why they can be used.

For most use cases, entities are not needed for AI Commerce Search. However, retailers who serve multiple brands or regions from a single product catalog can get better results if they use entities.

## Overview

Setting up multiple entities in your project is a way to take into consideration different behavior and preferences of shoppers who are in different regions or countries or who shop at differently branded sites that belong to your enterprise.

## Example use case: two countries

A retailer, Example Organization, has a web presence in both the US and Canada.

Example Organization wants to serve browse and search results and autocomplete suggestions that take into account differences between the shoppers in the two countries. And so, Example Organization designates two entities: `org_us` and `org_ca`.

User events are tagged with an entity value, depending on which website the shopper visited (`.com` or `ca`). When a shopper makes a search request, the entity value is included in the request.

The two countries have important but different holidays in July. With entities set up, when shoppers search the Example Organization site for `July`, American shoppers are served Fourth of July themed items first and Canadian shoppers receive items themed for Canada Day.

Similarly, recommendations for Canadian shoppers are more likely to show Canada Day items than Fourth of July items.

## Example use case: an acquisition

Enterprise Example Organization recently acquired Startup Example Organization. The catalogs have been combined but the Startup brand and website is being kept because it has a loyal following.

The enterprise creates an entity, `startup`, to tag user events originating from the Startup site. This allows the search, browse, autocomplete, and recommendation suggestions that are served to the Startup site to take into account the preferences of the Startup site's shoppers.

## Multiple projects or multiple entities?

When you set up AI Commerce Search, you can use different projects or different entities in the same project to get different suggestions for your different shopper populations.

For some applications, separate projects are required. For other applications, setting up entities is the better solution.

Use **entities** when you have:

  * A fully or partially shared catalog between the entities

  * One or more of the following:

    * Multiple brands in the same country or language area—for example, you have your original brand and an acquired brand, `google_home` and `nest`.

    * Multiple regions in the same country—for example, `enterprise_east` and `enterprise_west`.

    * One brand but in multiple countries with the same language—for example, `brand_us` and `brand_ca`.




Use **separate projects** instead of entities when you have:

  * Catalogs that cannot be combined or catalogs that, if combined, have little or no overlap.

  * Entities that require different languages. Only one language is allowed per project.




## User events and entities

To take advantage of the entities feature, add the entity field to your user events.

  * **For search and autocomplete:** include the [`entity`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents#UserEvent.FIELDS.entity) field in user events of type `search`.

Including the entity field in other user event types can be helpful for troubleshooting but does not affect the quality of the search or autocomplete responses.

  * **For recommendations:** Entities are not supported, but they can be added as a custom attribute in user events.




Typically, it takes 30 to 90 days of user event data before the entity feature returns optimal suggestions.

If an entity is missing from a request, the request makes no assumption about the entity in the result. You'll get an average result that is based on user events with and without the entity specified.

## Search and entities

To get search or browse results that take into account the entity:

  1. Include the [`entity`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents#UserEvent.FIELDS.entity) field in your search user events (`eventType="search"`). For an example, see the complete object example for the [Search](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/user-events#search) user event.

  2. Add the `entity` field to your search request. For information about how to make search requests, see [Get search results](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/search-basic).




## Autocomplete and entities

To get autocomplete results that take into account the entity:

  * Follow the instructions in [Auto-learning dataset](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/completion-overview#generated-completion-dataset) and [Suggestion filtered by entity](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/completion-overview#entity).



## Recommendations and entities

While Recommendations doesn't support the entities feature, as a workaround, the [`entity`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents#UserEvent.FIELDS.entity) field can be added as a custom attribute, which can be included in the call to the [predict](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.placements/predict) method.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
