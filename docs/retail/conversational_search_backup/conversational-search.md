---
url: https://docs.cloud.google.com/retail/conversational_search_backup/conversational-search/
title: Conversational agent overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T04:52:38.020865+00:00
---

# Conversational agent overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/retail/conversational_search_backup/conversational-search/




#  Conversational agent overview Stay organized with collections  Save and categorize content based on your preferences. 

This page describes AI Commerce Search Conversational agent, which is a guided search capability. The Conversational agent capability functions as part of the guided search package, providing users with a real-time, ongoing conversational experience that's more interactive.

![Shopping agent chat interaction](https://docs.cloud.google.com/static/retail/docs/images/what-is-conversational-search.png)

![](https://docs.cloud.google.com/static/retail/docs/images/what-is-conversational-search.png)

## What is Conversational agent?

Conversational agent is an AI-driven guided search and product discovery tool. Instead of searching with keywords, users utilize natural language to ask for what they need, which includes follow up questions, multimodal interactions, improved intent understanding, and grounding with data beyond the product catalog.

**Note:** You can't trigger Conversational agent from [browse searches](https://docs.cloud.google.com/retail/docs/search-basic#browse-searches).

  * **Use case** : Handles natural language queries beyond core product searches.

    * _Help me plan a party_
    * _Compare 1% and 2% milk_
    * _What are the best running shoes for trails?_
  * **Key difference from conversational product filtering** : Provides AI-generated text answers and understands broader user intent.

  * **Remember the architecture** : The two-API model is still in effect. You must call the Search API to get product results based on suggestions from the Conversational API.




## Conversational agent capabilities

Conversational agent adds to the AI Commerce Search experience in the following ways:

  * **Narrows user queries effectively** : Conversational agent filters 10,000 products down to less than 100 products, increasing the likelihood that the user decides to make a purchase.
  * **Hyper-personalization** : Search agents analyze shoppers' preferences, purchase history, and social media activity to provide more personalized product recommendations, promotions, and shopping experiences.
  * **Integrated end-to-end journeys** : From product discovery to checkout, the search agents accompany the end user along their entire shopping journey with immersive, dynamic, and continuous conversation.
  * **Adapted to commerce use case** : Conversational agent covers ecommerce, product discovery, and support.
  * **Immersive user experiences** : With the help of search agents threading user conversations, augmented and virtual reality can be additionally implemented on the merchant site to create virtual try-ons, store tours, and spatial product visualization.



![Conversational agent improves user conversion](https://docs.cloud.google.com/static/retail/docs/images/add-value.png)

![](https://docs.cloud.google.com/static/retail/docs/images/add-value.png)

## Impact of Conversational agent

As a central part of the guided search package, Conversational agent improves search result relevance and reduces user friction.

Customary commerce search is the most common way to find products. Customary approaches rely on rigid keyword matching, which requires your users to use specific words and manually adjust filters to refine results. However, only [**1 in 10 consumers**](https://cloud.google.com/blog/topics/retail/new-research-on-search-abandonment-in-retail) say that they find exactly what they're looking for when using legacy keyword-based search.

Conversational agent solves the most frustrating problems for users when searching, such as inexact matches, irrelevant results, or zero-return queries.

### Natural language understanding

AI-powered search recognizes full-phrase queries, interprets intent and accounts for variation in language.

![Anatomy of a search query](https://docs.cloud.google.com/static/retail/docs/images/anatomy-search-query.png)

![](https://docs.cloud.google.com/static/retail/docs/images/anatomy-search-query.png)

### Predictive assistance

Helps users formulate queries more effectively by suggesting completions as they type.

![Predictive assistance suggests completions as users type](https://docs.cloud.google.com/static/retail/docs/images/predictive-assistance.png)

![](https://docs.cloud.google.com/static/retail/docs/images/predictive-assistance.png)

### Multimodal inputs

![Image showing multimodal inputs](https://docs.cloud.google.com/static/retail/docs/images/multimodal-inputs2.png)![](https://docs.cloud.google.com/static/retail/docs/images/multimodal-inputs2.png)

Conversational agent enables users to search using multimodal input methods, such as voice and image, in addition to text. It understandings user intent, context and natural language variations in phrasing without losing context.

  * **Voice search** : Spoken queries are often structured differently than typed ones. AI Commerce Search processes these variations while accounting for variables like accents, background noise and "um's," "uh's" and "like's." For mobile, voice search is not only easier to input, but it can also take up less screen space, allowing more real estate product visuals.
  * **Image search** : Image recognition makes it faster to find a similar or unique item on a social media post or by snapping a picture in real life. Shoppers can then use image search to quickly search and locate a similar item on your site.
![Image search mobile screen](https://docs.cloud.google.com/static/retail/docs/images/image-search.png)![](https://docs.cloud.google.com/static/retail/docs/images/image-search.png)


### Mobile-first experience

Nearly 80% of all ecommerce visits worldwide occurred on a mobile phone in 2024. Smaller screens, shorter user sessions and clustered menus create unique challenges for legacy search experiences. Conversational agent is designed to enable users to access the full power of AI-driven search from their mobile devices. 

### The role of external search and AI assistants

When a user has a preferred retailer, they tend to go directly to it. However, when exploring new or broader options, the customer user journey is more likely to first start at a marketplace orientation, such as Google Search or an AI assistant.

As AI-driven search evolves, the AI Commerce Search guided search package bridges the gap between external and on-site product discovery. By treating the transition to the commerce site as a single, fluid conversation, Conversational agent ensures users find relevant results quickly.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
