---
url: https://docs.cloud.google.com/retail/conversational_search_backup/conversational-agents-both-features/
title: Conversational commerce \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:12:44.384140+00:00
---

# Conversational commerce  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/retail/conversational_search_backup/conversational-agents-both-features/




#  Conversational commerce Stay organized with collections  Save and categorize content based on your preferences. 

AI Commerce Search offers two conversational capabilities: conversational product filtering and the Conversational agent. Conversational product filtering guides users with structured questions to refine searches, while the Conversational agent enables open-ended chat experiences.

## Two conversational capabilities with a single API endpoint

Both capabilities are powered by the `conversationalSearch` API endpoint.

### Conversational product filtering

  * **Use case:** Guides users to refine broad searches, such as _dress_ , with clarifying questions like **What is the color?**

  * **Interaction model:** Reflects structured, multiple-choice questions and answers.




For more information about conversational filtering, see the [Conversational product filtering](https://docs.cloud.google.com/retail/docs/conversational-filtering) section.

### Conversational agent

  * **Use case:** Enables open-ended, natural language chat experiences like _Help me plan a party_.

  * **Interaction model:** Includes AI-generated text responses, dynamic search suggestions, and follow-up questions.




For more information about the interactive Conversational agent capability, see the [Conversational agent](https://docs.cloud.google.com/retail/docs/conversational-search) section.

## Both capabilities enable conversations with parallel API calls

The Conversational API **does not** return product search results. Its purpose is to provide the conversational experience.

Your application must make two separate, parallel API calls for each user interaction. This architecture is fundamental to both product filtering and the Conversational agent.

The Conversational API:

  * Has the endpoint `conversationalSearch`.
  * Enables follow-up questions, text responses, and refined queries.
  * Returns fields including `conversation_id`, `followup_question`, and `conversational_text_response`.



The Search API:

  * Has the endpoint `search`.
  * Gets the list of products to display to the user.
  * Returns a standard list of product results.



## Both capabilities use the core field `conversation_id`

The `conversation_id` is the key to maintaining the state and history of a single conversation session.

  * **First request:** Sends the initial query with no `conversation_id`.
  * **Response:** The API returns a new `conversation_id`.
  * **Your action:** Store this in client-side session storage.
  * **Subsequent requests:** For all follow-up interactions within the same session, you must send the stored `conversation_id` in the request. This allows the system to understand context, such as _the user already said they want a yellow dress_.

**Note:** A conversation is started with just a request without a `conversation_id`.

## What's next

  * Set up and use [conversational product filtering](https://docs.cloud.google.com/retail/docs/conversational-filtering).
  * Set up and use the [Conversational agent](https://docs.cloud.google.com/retail/docs/conversational-search).



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
