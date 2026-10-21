---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/translation/rpc/google.cloud.translation.v3
title: Package google.cloud.translation.v3 \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:16:12.036405+00:00
---

# Package google.cloud.translation.v3  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/translation/rpc/google.cloud.translation.v3

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/reference/reference-overview)



Send feedback 

#  Package google.cloud.translation.v3 Stay organized with collections  Save and categorize content based on your preferences. 

Important: To access the URL listed within parentheses, you must connect to the internet. The URL is provided to access outside of your air-gapped environment. 

## TranslationService

Provides natural language translation operations.

DetectLanguage  
---  
` rpc DetectLanguage(`[DetectLanguageRequest](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/translation/rpc/google.cloud.translation.v3#google.cloud.translation.v3.DetectLanguageRequest)`) returns (`[DetectLanguageResponse](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/translation/rpc/google.cloud.translation.v3#google.cloud.translation.v3.DetectLanguageResponse)`) ` Detects the language of text within a request.  
GetSupportedLanguages  
---  
` rpc GetSupportedLanguages(`[GetSupportedLanguagesRequest](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/translation/rpc/google.cloud.translation.v3#google.cloud.translation.v3.GetSupportedLanguagesRequest)`) returns (`[SupportedLanguages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/translation/rpc/google.cloud.translation.v3#google.cloud.translation.v3.SupportedLanguages)`) ` Returns a list of supported languages for translation.  
TranslateText  
---  
` rpc TranslateText(`[TranslateTextRequest](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/translation/rpc/google.cloud.translation.v3#google.cloud.translation.v3.TranslateTextRequest)`) returns (`[TranslateTextResponse](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/translation/rpc/google.cloud.translation.v3#google.cloud.translation.v3.TranslateTextResponse)`) ` Translates input text and returns translated text.  
  
## DetectLanguageRequest

The request message for language detection.

Fields  
---  
`parent` |  `string` Required. Project to make a call. Must refer to a caller's project.Format: `projects/{project-id}.`  
`mime_type` |  `string` Optional. The format of the source text, for example, "text/html", "text/plain". If left blank, the MIME type defaults to "text/html".  
`content` |  `string` The content of the input stored as a string.  
  
## DetectLanguageResponse

The response message for language detection.

Fields  
---  
`languages[]` |  ``[DetectedLanguage](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/translation/rpc/google.cloud.translation.v3#google.cloud.translation.v3.DetectedLanguage)`` The most probable language detected by the Translation API. For each request, the Translation API will always return only one result.  
  
## DetectedLanguage

The response message for language detection.

Fields  
---  
`language_code` |  `string` The BCP-47 language code of source content in the request, detected automatically.  
`confidence` |  `float` The confidence of the detection result for this language.  
  
## S3Source

The storage location for the input content.

Fields  
---  
`input_uri` |  `string` Required. Source data URI. For example, `s3://my_bucket/my_object`.  
  
## GetSupportedLanguagesRequest

The request message for discovering supported languages.

Fields  
---  
`parent` |  `string` Required. Project to make a call. Must refer to a caller's project.Format: `projects/{project-id}`.  
`display_language_code` |  `string` Optional. The language to use to return localized, human-readable names of supported languages. If missing, then display names aren't returned in a response.  
  
## SupportedLanguage

A single supported language response corresponds to information related to one supported language.

Fields  
---  
`language_code` |  `string` Supported language code, generally consisting of its ISO 639-1 identifier, for example, 'en', 'ja'. In certain cases, BCP-47 codes including language and region identifiers are returned (for example, 'zh-TW' and 'zh-CN')  
`display_name` |  `string` Human-readable name of the language localized in the display language specified in the request.  
`support_source` |  `bool` Can be used as source language.  
`support_target` |  `bool` Can be used as target language.  
  
## SupportedLanguages

The response message for discovering supported languages.

Fields  
---  
`languages[]` |  ``[SupportedLanguage](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/translation/rpc/google.cloud.translation.v3#google.cloud.translation.v3.SupportedLanguage)`` A list of supported language responses. This list contains an entry for each language the Translation API supports.  
  
## TranslateTextRequest

The request message for synchronous translation.

Fields  
---  
`contents[]` |  `string` Required. The content of the input in string format. We recommend the total content be less than 30k codepoints. The max length of this field is 1024.  
`mime_type` |  `string` Optional. The format of the source text, for example, "text/html", "text/plain". If left blank, the MIME type defaults to "text/html".  
`source_language_code` |  `string` The BCP-47 language code of the input text if known, for example, `en-US` or `sr-Latn`. Supported language codes are listed in Language Support.  
`target_language_code` |  `string` Required. The BCP-47 language code to use for translation of the input text, set to one of the language codes listed in Language Support.  
`parent` |  `string` Required. Project to make a call. Must refer to a caller's project.Format: `projects/{project-id}`  
  
## TranslateTextResponse

Fields  
---  
`translations[]` |  ``[Translation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/translation/rpc/google.cloud.translation.v3#google.cloud.translation.v3.Translation)`` Text translation responses. This field has the same length as `[`contents`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/translation/rpc/google.cloud.translation.v3#google.cloud.translation.v3.TranslateTextRequest.FIELDS.repeated.string.google.cloud.translation.v3.TranslateTextRequest.contents)`.  
  
## Translation

A single translation response.

Fields  
---  
`translated_text` |  `string` Text translated into the target language. If an error occurs during translation, this field might be excluded from the response.  
`detected_language_code` |  `string` If the source language was passed, auto-detection of the language doesn't occur and this field is empty.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-11 UTC."],[],[]] 
