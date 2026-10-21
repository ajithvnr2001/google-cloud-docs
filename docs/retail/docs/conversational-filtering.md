---
url: https://docs.cloud.google.com/retail/docs/conversational-filtering/
title: Conversational product filtering overview \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:20:17.792933+00:00
---

# Conversational product filtering overview  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/retail/docs/conversational-filtering/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Conversational product filtering overview Stay organized with collections  Save and categorize content based on your preferences. 

This page serves as a guide to implement conversational product filtering for AI Commerce Search. This document provides data-backed best practices to ensure a successful implementation of conversational product filtering for mid-to-large retail businesses.

AI Commerce Search conversational product filtering is an AI-powered tool that transforms search into a guided experience to accompany shoppers when they interact with large product catalogs. When a site user performs a broad search (like _coffee table_ or _red dress)_ that returns thousands of results, conversational product filtering intelligently prompts them with follow-up questions to quickly narrow down their options.

## Business use case

The conversational product filtering capability in guided search is specifically designed to address broad, ambiguous or very nuanced search queries. Applying filters to narrow the results significantly increases both revenue and user engagement.

The primary goal of conversational product filtering is to help shoppers find the right items quickly and intuitively.

Businesses use conversational filtering to:

  * **Accelerate product discovery** : Help shoppers quickly narrow down vast product selections (such as going from 5,000 _area rugs_ to a few hundred targeted results) by asking relevant questions.
  * **Refine personalization** : The questions and multiple-choice options are custom for every query, based on historical filter usage data for that specific query (_coffee table_ is historically filtered by color more often than size, so color can be asked first).
  * **Simplify implementation** : Questions are predesignated for product attributes, such as color and width, with one question per attribute.



## One-way conversation

Conversational product filtering operates as a one-way conversation that accompanies the shopper throughout their search journey on an ecommerce site. The AI model asks the shopper a question, and the shopper answers.

  1. The shopper initiates a search query, such as _area rugs._

  2. The retail site returns 80+ pages of product results.

  3. AI Commerce Search asks the shopper on the site a question to help narrow their search. Example: **Which color are you looking for?**

  4. The shopper selects an answer from a list of multiple-choice options. Example: **blue**

  5. The product results on the page are immediately filtered based on the shopper's selection.

  6. Search then presents the next most relevant follow-up question. Example: **What shape are you looking for?**


**Note:** Browse only has the multiple-choice option, while AI Commerce Search has full conversational search capabilities.

![Conversational search user journey](https://docs.cloud.google.com/static/gemini-enterprise-cx/ai-commerce-search/images/user-journey.png)**Figure 1**. Conversational filtering user journey.

### Question generation

The AI examines attribute names and values from the product catalog and generates one question per attribute.

#### Example

  * Attribute name: `Coffee table shape`
  * Values: `"Round"`, `"Square"`, `"Oval"`
  * Generated question: **What shape table do you want?**



### Edit and approve questions

Retailers review and edit the generated questions for relevance and tone.

#### Example

  * Skip question: **How much do you weigh?** (Irrelevant/unsafe)
  * Edit question: **What shape~~table do you want?~~** → **What shape are you shopping for?** (Improved phrasing)



### Conversation planning

The AI utilizes customer filter usage data to determine the optimal order of questions and the best multiple-choice options.

#### Example

  * Customer query: _Coffee table_
  * Question #1: Shape (the most frequently used filter)
  * Multiple-choice options: **Oval** , **Square** , and **Round**



### Question serving

The generated questions and multiple-choice options are returned to the user in the same API response as the product results.

#### Visual example in the chat interface

  * **AI** :



What shape are you looking for?

  * **Options** :



Round Rectangular Oval Square Triangle Corner

### Answer processing

The system processes both multiple-choice selections and user-entered answers.

The user then takes one of these actions:

  * Customer chooses multiple choice → `<Add a filter>`
  * Customer types own answer → `<Run synthetic query>`



## Iterative improvement with testing

Conversational product filtering is optimization that requires continuous refinement and data-driven decisions. The goal is to maximize the feature capability of gathering user insights by understanding shopper behavior and adapting the design to foster user traction.

Influenced by various factors, such as market trends, competitor offerings, and changes in personal preferences, shopper behaviors are dynamic and evolve over time. It's important to continue to experiment and iterate on your design, and test new approaches as you gather more data and observe how shoppers interact with the AI features. This ongoing cycle of experimentation, data analysis, and refinement helps to ensure that the AI features remain relevant, effective, and optimized for your evolving user base.

Regularly review performance metrics, conduct user surveys, and analyze feedback to identify areas for improvement and new opportunities for innovation. This commitment to continuous iteration is key to long-term success in AI feature deployment.

### Lessons learned

The following lessons learned occur after successive testing:

  * **Experiment continuously** : The optimal result is often not the first design you try.
  * **Iterate and adapt** : User behaviors evolve. Continue to iterate on your designs and test new approaches as you gather more data and observe how shoppers interact with the feature.
  * **Beyond A/B** : Don't limit yourself to just A/B testing, which compares two versions. Instead, conduct many A/B/C/D/E/F tests to explore a wider range of UI designs and placement options.



### Key metrics for optimization

To effectively optimize AI Commerce Search, it's crucial to define and track relevant metrics that provide insights into user engagement, satisfaction, and the overall impact of the features. Key metrics to consider include the following:

  * **Conversion rate** : The percentage of users who complete the targeted action, such as making a purchase.
  * **User satisfaction scores (such as NPS, CSAT)** : Direct feedback from users on their experiences with the AI feature that provides qualitative insights into usability and perceived value.
  * **Adoption rate** : The percentage of shoppers that actively use conversational product filtering that indicates its visibility and perceived utility.



## Follow-up questions in search

**Note:** The model doesn't answer questions from the shopper. For this functionality, it is recommended to implement [ćonversational commerce](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/conversational-search), which is distinct from product filtering capability.

If conversational product filtering is enabled, follow-up questions on the site drive a conversation that ensues until one of the three following scenarios occur:

  * A preconfigured minimum product count is reached (a conversation is not useful when only two products show up).
  * The user clicks on a product and adds it to their cart (the objective).
  * Conversational product filtering runs out of AI-generated questions.



## Use as an alternative to dynamic facets

Dynamic facets are associated with broad queries and resulting high search return counts, which leads to low revenue per query. End users can become overwhelmed when they see tens of thousands of results and abandon the search. Conversational search is able to refine queries and can be used with dynamic facets. Conversational product filtering offers some advantages over dynamic facets, being more human, more interactive, and using less on-page real estate.

For more information, refer to the [Facets](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/facets-overview) page.

## Edit generative questions

Conversational product filtering encourages a human-in-the-loop interaction with the generative AI questions by allowing retailers to preliminarily edit, overwrite, or deselect AI-generated questions according to their preferences, based on the uploaded catalog. Questions can be edited or disabled individually or in bulk in the AI Commerce Search in Gemini Enterprise for Customer Experience console or the API in order to tailor the questions they want to appear in the search.

## Conclusion

The integration of conversational product filtering within your commerce platform provides a way to significantly enhance the user experience and drive a substantial increase in user conversion rates. This is true for broad category queries, where your users often face an overwhelming array of choices and struggle to quickly narrow down their preferences.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
