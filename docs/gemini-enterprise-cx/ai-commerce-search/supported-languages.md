---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/supported-languages/
title: Supported world languages \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:33.436403+00:00
---

# Supported world languages  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/supported-languages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Supported world languages Stay organized with collections  Save and categorize content based on your preferences. 

Search and recommendations both support the following world languages.

## Search for commerce

View supported languages

Supported languages  
---  
Albanian| Korean  
Arabic| Latvian  
Armenian| Lithuanian  
Assamesse| Macedonian  
Azerbaijani| Malay  
Basque| Marathi  
Bengali (Bangla)| Mongolian  
Bulgarian| Nepali  
Burmese| Norwegian  
Catalan| Odia  
Chinese (simplified)| Persian  
Chinese (traditional)| Polish  
Croatian| Portuguese (Europe)  
Czech| Portuguese (Brazil)  
Danish| Punjabi  
Dutch| Romanian  
English| Russian  
Estonian| Serbian  
Finnish| Serbian (Cyrillic)  
French (Europe)| Sinhala  
French (Canada)| Slovak  
Georgian| Slovenian  
German| Spanish (Europe)  
Greek| Spanish (Latin America)  
Gujarati| Swahili  
Hebrew| Swedish  
Hindi| Tamil  
Hungarian| Telugu  
Icelandic| Thai  
Indonesian| Turkish  
Italian| Ukrainian  
Japanese| Urdu (India)  
Kannada| Urdu (Pakistan)  
Kazakh| Uzbek  
Khmer| Vietnamese  
  
### Mixed language settings

You set the language when you upload your catalog for your AI Commerce Search project. The catalog should be in one language only, and search queries should be sent in the same language. Having multiple languages in the catalog can degrade LLM performance.

To avoid this and to continue to optimize your search events in multiple languages, you have two options:

  * For any low-traffic and unusual languages, you can route those queries to the main project. AI Commerce Search auto-translates those queries.
  * If you have a lot of traffic in some other language and know which users these queries are associated to, have two projects, one in each language, and have the associated queries routed accordingly.

**Note:** If you already have a mixed language catalog for search, you can also improve results by adding synonyms for search query terms. For example, add both Spanish and English synonyms. For information about synonyms, see [OnewaySynonymsAction](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#onewaysynonymsaction) and [TwowaySynonymsAction](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rpc/google.cloud.retail.v2#twowaysynonymsaction).

## Recommendations

Most languages are supported. The model automatically detects the text language.

View supported languages

Language Name | Script Name  
---|---  
Afrikaans | Latin  
Amharic | Ethiopic  
Arabic | Arabic  
Bulgarian | Cyrillic  
Bulgarian | Latin  
Bangla | Bangla  
Bosnian | Latin  
Catalan | Latin  
Cebuano | Latin  
Corsican | Latin  
Czech | Latin  
Welsh | Latin  
Danish | Latin  
German | Latin  
Greek | Greek  
Greek | Latin  
English | Latin  
Esperanto | Latin  
Spanish | Latin  
Estonian | Latin  
Basque | Latin  
Persian | Arabic  
Finnish | Latin  
Filipino | Latin  
French | Latin  
Western Frisian | Latin  
Irish | Latin  
Scottish Gaelic | Latin  
Galician | Latin  
Gujarati | Gujarati  
Hausa | Latin  
Hawaiian | Latin  
Hindi | Devanagari  
Hindi | Latin  
Hmong | Latin  
Croatian | Latin  
Haitian Creole | Latin  
Hungarian | Latin  
Armenian | Armenian  
Indonesian | Latin  
Igbo | Latin  
Icelandic | Latin  
Italian | Latin  
Hebrew | Hebrew  
Japanese | Japanese  
Japanese | Latin  
Javanese | Latin  
Georgian | Georgian  
Kazakh | Cyrillic  
Khmer | Khmer  
Kannada | Kannada  
Korean | Korean  
Kurdish | Latin  
Kyrgyz | Cyrillic  
Latin | Latin  
Luxembourgish | Latin  
Lao | Lao  
Lithuanian | Latin  
Latvian | Latin  
Malagasy | Latin  
Maori | Latin  
Macedonian | Cyrillic  
Malayalam | Malayalam  
Mongolian | Cyrillic  
Marathi | Devanagari  
Malay | Latin  
Maltese | Latin  
Burmese | Myanmar  
Nepali | Devanagari  
Dutch | Latin  
Norwegian | Latin  
Nyanja | Latin  
Punjabi | Gurmukhi  
Polish | Latin  
Pashto | Arabic  
Portuguese | Latin  
Romanian | Latin  
Russian | Cyrillic  
Russian | English  
Sindhi | Arabic  
Sinhala | Sinhala  
Slovak | Latin  
Slovenian | Latin  
Samoan | Latin  
Shona | Latin  
Somali | Latin  
Albanian | Latin  
Serbian | Cyrillic  
Southern Sotho | Latin  
Sundanese | Latin  
Swedish | Latin  
Swahili | Latin  
Tamil | Tamil  
Telugu | Telugu  
Tajik | Cyrillic  
Thai | Thai  
Turkish | Latin  
Ukrainian | Cyrillic  
Urdu | Arabic  
Uzbek | Latin  
Vietnamese | Latin  
Xhosa | Latin  
Yiddish | Hebrew  
Yoruba | Latin  
Chinese | Han (including Simplified and Traditional)  
Chinese | Latin  
Zulu | Latin  
  
For a list of all languages that can be automatically detected, see the Compact Language Detector [GitHub README](https://github.com/google/cld3#supported-languages).

## Language normalization and tokenization

The AI Commerce Search engine has built-in processing of Chinese or Japanese characters without spaces and normalizes European diacritics. This eliminates the need to build proprietary pre-processing translation layers into your search applications.

  * **Non-English character normalization** : The search engine provides built-in support of UTF-8 and automatically normalizes diacritics and umlauts during indexing and querying (such as mapping `ä` to `a` or `ae`, and `é` to `e`). This allows users to search for _cafe_ and seamlessly find _café._
  * **CJK tokenization (Kanji and Katakana)** : For Chinese, Japanese, and Korean (CJK) languages, the engine doesn't rely on spaces for tokenization. It utilizes dictionary-based segmenters and morphological analyzers to break strings of Kanji, Hiragana, Katakana, or Han characters into logical, searchable tokens.
  * **Strict single-language rule** : Your catalog and your search queries must be in the same language. A Spanish query won't match against an English catalog. Mixing languages can degrade the model's performance.
  * **Multilingual workaround** : If a catalog must support mixed-language queries, use the `twowaySynonymsAction` or `onewaySynonymsAction` controls to manually map custom query terms (such as Spanish synonyms) to the default catalog language (such as English).



For more about language settings, see [About catalogs and products](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/catalog#language_settings).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
