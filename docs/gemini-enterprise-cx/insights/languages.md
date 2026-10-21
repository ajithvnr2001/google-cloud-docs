---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/languages/
title: Language support \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:11:07.504769+00:00
---

# Language support  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/languages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Language support Stay organized with collections  Save and categorize content based on your preferences. 

This page lists all languages supported by Customer Experience Insights. Language is specified within a conversation's [`languageCode`](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations#Conversation) parameter. This field is distinct from the utterance-level [`languageCode`](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations#transcriptsegment) field, which you can optionally set in a `TranscriptSegment` object to assign a language to that specific utterance in the transcript. CX Insights uses the conversation-level [`languageCode`](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations#Conversation) to determine whether the features listed next to the [Language Table](https://docs.cloud.google.com/gemini-enterprise-cx/insights/languages#table) check boxes are supported by your language. If the conversation-level `languageCode` is not set, CX Insights infers the language from the utterance-level `languageCode` (if set) and then from detecting the transcript's language directly. For more information about creating and analyzing conversations, see the [console guide](https://docs.cloud.google.com/gemini-enterprise-cx/insights/create-analyze-conversation-ui) or the [REST API guide](https://docs.cloud.google.com/gemini-enterprise-cx/insights/create-analyze-conversation-api). 

##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how CX Insights performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try CX Insights free ](https://console.cloud.google.com/freetrial)

## Language table

CX Insights supports the languages listed in the table for the following features:

  * [Conversation storage and import](https://docs.cloud.google.com/gemini-enterprise-cx/insights/create-analyze-conversation-ui#upload)
  * [Create topic model](https://docs.cloud.google.com/gemini-enterprise-cx/insights/topic-modeling-basics#topic_models)
  * [Custom highlights](https://docs.cloud.google.com/gemini-enterprise-cx/insights/custom-highlights-ui)
  * Entity
  * [Infer topics](https://docs.cloud.google.com/gemini-enterprise-cx/insights/topic-modeling-basics#topic_inference)
  * Intent and [Smart highlights](https://docs.cloud.google.com/gemini-enterprise-cx/insights/smart-highlights)
  * [Quality AI](https://docs.cloud.google.com/gemini-enterprise-cx/insights/quality-ai)
  * [Summarization](https://docs.cloud.google.com/gemini-enterprise-cx/insights/summarization) (Supports the same languages as [Agent Assist summarization](https://docs.cloud.google.com/agent-assist/docs/languages).)

**Note:** The interruption and silence features measure when someone stops speaking, so they don't require specific language support.

You can filter the following table to see which languages and dialects are available for the feature(s) that you want to use by selecting the checkbox next to the feature's name. The filtered table only shows the languages and dialects which all of your selected features support. 

All

Store & Import conversations ([using API or console](https://docs.cloud.google.com/gemini-enterprise-cx/insights/create-analyze-conversation-ui#upload))

Create a topic model

Infer topics

Quality AI

Intent & Smart highlights

Custom highlights

Entity

Name | BCP-47 | Store/Import | Create a topic model | Infer topics | Quality AI | Intent/Smart highlights | Custom highlights | Entity  
---|---|---|---|---|---|---|---|---  
Afrikaans | af |  |  |  |  |  |  |   
Albanian | sq |  |  |  |  |  |  |   
Amharic | am |  |  |  |  |  |  |   
Arabic | ar |  |  |  |  |  |  |   
Armenian | hy |  |  |  |  |  |  |   
Azerbaijani | az |  |  |  |  |  |  |   
Basque | eu |  |  |  |  |  |  |   
Bengali | bn |  |  |  |  |  |  |   
Bosnian | bs |  |  |  |  |  |  |   
Bulgarian | bg |  |  |  |  |  |  |   
Burmese | my |  |  |  |  |  |  |   
Catalan | ca |  |  |  |  |  |  |   
Chinese, Cantonese | yue |  |  |  |  |  |  |   
Chinese, Mandarin | zh |  |  |  |  |  |  |   
Croatian | hr |  |  |  |  |  |  |   
Czech | cs |  |  |  |  |  |  |   
Danish | da |  |  |  |  |  |  |   
Dutch | nl |  |  |  |  |  |  |   
English | en |  |  |  |  |  |  |   
Estonian | et |  |  |  |  |  |  |   
Filipino | fil |  |  |  |  |  |  |   
Finnish | fi |  |  |  |  |  |  |   
French | fr |  |  |  |  |  |  |   
Galician | gl |  |  |  |  |  |  |   
Georgian | ka |  |  |  |  |  |  |   
German | de |  |  |  |  |  |  |   
Greek | el |  |  |  |  |  |  |   
Gujarati | gu |  |  |  |  |  |  |   
Hebrew | iw |  |  |  |  |  |  |   
Hindi | hi |  |  |  |  |  |  |   
Hungarian | hu |  |  |  |  |  |  |   
Icelandic | is |  |  |  |  |  |  |   
Indonesian | id |  |  |  |  |  |  |   
Italian | it |  |  |  |  |  |  |   
Japanese | ja |  |  |  |  |  |  |   
Javanese | jv |  |  |  |  |  |  |   
Kannada | kn |  |  |  |  |  |  |   
Kazakh | kk |  |  |  |  |  |  |   
Khmer | km |  |  |  |  |  |  |   
Korean | ko |  |  |  |  |  |  |   
Lao | lo |  |  |  |  |  |  |   
Latvian | lv |  |  |  |  |  |  |   
Lithuanian | lt |  |  |  |  |  |  |   
Macedonian | mk |  |  |  |  |  |  |   
Malay | ms |  |  |  |  |  |  |   
Malayalam | ml |  |  |  |  |  |  |   
Marathi | mr |  |  |  |  |  |  |   
Mongolian | mn |  |  |  |  |  |  |   
Nepali | ne |  |  |  |  |  |  |   
Norwegian Bokmål | no |  |  |  |  |  |  |   
Persian | fa |  |  |  |  |  |  |   
Polish | pl |  |  |  |  |  |  |   
Portuguese | pt |  |  |  |  |  |  |   
Punjabi | pa |  |  |  |  |  |  |   
Romanian | ro |  |  |  |  |  |  |   
Russian | ru |  |  |  |  |  |  |   
Serbian | sr |  |  |  |  |  |  |   
Sinhala | si |  |  |  |  |  |  |   
Slovak | sk |  |  |  |  |  |  |   
Slovenian | sl |  |  |  |  |  |  |   
Spanish | es |  |  |  |  |  |  |   
Sundanese | su |  |  |  |  |  |  |   
Swahili | sw |  |  |  |  |  |  |   
Swedish | sv |  |  |  |  |  |  |   
Tamil | ta |  |  |  |  |  |  |   
Telugu | te |  |  |  |  |  |  |   
Thai | th |  |  |  |  |  |  |   
Turkish | tr |  |  |  |  |  |  |   
Ukrainian | uk |  |  |  |  |  |  |   
Urdu | ur |  |  |  |  |  |  |   
Uzbek | uz |  |  |  |  |  |  |   
Vietnamese | vi |  |  |  |  |  |  |   
Zulu | zu |  |  |  |  |  |  |   
  
* |  Language tags follow the [HTTP/1.1 specification, section 3.10](https://tools.ietf.org/html/rfc2616#section-3.10).   
---|---  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
