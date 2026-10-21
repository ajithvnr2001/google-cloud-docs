---
url: https://docs.cloud.google.com/dialogflow/es/docs/agents-multilingual/
title: Multilingual agents \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:45:36.232473+00:00
---

# Multilingual agents  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/agents-multilingual/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Multilingual agents Stay organized with collections  Save and categorize content based on your preferences. 

Dialogflow supports many languages. For the complete list, see the [languages reference page](https://docs.cloud.google.com/dialogflow/es/docs/reference/language). The language you choose when creating an agent is set as the default language, and you can add additional languages.

## Root and locale-specific languages

There are two categories of languages:

  * **Root languages** : These are languages like _English (en)_ that do not specify a locale.
  * **Locale-specific languages** : These are languages like _English-US (en-US)_ that do specify a locale as a specific region or country.



Some languages act as both root and locale-specific. There are significant differences between locales for these languages, so the locales cannot share a common root language. Examples:

  * Chinese-Cantonese (zh-HK)
  * Chinese-Simplified (zh-CN)
  * Chinese-Traditional (zh-TW)
  * Portuguese-Brazil (pt-BR)
  * Portuguese-Portugal (pt)



You should primarily design your agent for root languages, and only customize for locale-specific languages as needed.

## Add a language

**Note:** As a best practice, you should complete your agent in the default language before adding additional languages.

To add a language or locale with the Dialogflow ES console Console:

  1. In the left sidebar menu, click the add language _add_ button next to the existing language(s). ![](https://docs.cloud.google.com/static/dialogflow/es/docs/images/add-a-language.png)  
This takes you to the **Languages** tab of agent settings.
  2. Choose a language from the **Select Additional Language** dropdown menu.
  3. To add a locale, hover over a root language and click **\+ Add locale**.
  4. Click **Save**.



## Language-specific data

**Note:** The information in this section applies to both locale-specific and root languages. For example; `en`, `en-US`, and `en-GB` each have unique data for intent training phrases.

Most agent data is common for all languages of a multilingual agent. However, text used to interact with an end-user is language-specific. When building a multilingual agent, you must supply this language-specific data for each language. When you select a language from the console or provide a language to the API, you can access this language-specific data for the given language. The following is a complete list of language-specific data:

  * [intent training phrases](https://docs.cloud.google.com/dialogflow/es/docs/intents-training-phrases)
  * [intent responses](https://docs.cloud.google.com/dialogflow/es/docs/intents-responses)
  * [entity entries](https://docs.cloud.google.com/dialogflow/es/docs/entities-overview)



To access language-specific data with the console, click the language button under the agent name. 

For example, the _size_ entity type below is used for ordering t-shirts. The agent was originally configured in English, so the entity has entries like "S" with the synonym "small". When Spanish is added as a language, the entity is created by Dialogflow for the new language, but you need to supply entity entries in Spanish.

Entity | Synonyms  
---|---  
XS | XS, extra pequeño  
S | S, pequeño  
M | M, medio  
L | L, grande  
XL | XL, extra grande  
  
### Language-specific data when using the API

To access language-specific data with the API, provide the `languageCode` parameter when getting, creating, or updating [EntityType](https://docs.cloud.google.com/dialogflow/es/docs/reference/common-types#entitytypes) or [Intent](https://docs.cloud.google.com/dialogflow/es/docs/reference/common-types#intents) types. 

You must make separate API calls for each language to access all language-specific data. If your API calls update language-generic data, that data is updated for all languages.

## Test in the simulator

When using the [simulator](https://docs.cloud.google.com/dialogflow/es/docs/console#simulator), choose the language you want to use by selecting it below the agent name.

## Supply a language using the API

When sending requests via the API, set the `queryInput.input.languageCode` field of the `detectIntent` method. For more information, see the [`Sessions`](https://docs.cloud.google.com/dialogflow/es/docs/reference/common-types#sessions) type. 

## Requests that do not supply an agent's language

When Dialogflow receives a request that does not supply a language supported by the agent, the following rules apply:

  * When a request does not supply a language, Dialogflow automatically determines the input language and responds in that language **if automatic language detection is enabled**. If automatic language detection is disabled, Dialogflow handles the request using the default language.
  * When a request supplies a locale-specific language that is not supported by the agent, but the associated root language is supported by the agent, Dialogflow handles the request using the root language.
  * System entity extraction is an exception to the previous rule. System entity extraction uses the supplied locale-specific language, even if the locale-specific language is not supported by the agent.



## Integrations

Agent interactions through text-based and phone gateway [integrations](https://docs.cloud.google.com/dialogflow/es/docs/integrations) only use the default language of the agent.

[ Previous arrow_back  Versions and environments  ](https://docs.cloud.google.com/dialogflow/es/docs/agents-versions)

[ Next Mega agents  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/agents-mega)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
