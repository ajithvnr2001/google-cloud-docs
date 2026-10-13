---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.cloud.translation.v3
title: Package google.cloud.translation.v3 \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:34:39.489591+00:00
---

# Package google.cloud.translation.v3  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.cloud.translation.v3

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  Package google.cloud.translation.v3 Stay organized with collections  Save and categorize content based on your preferences. 

Important: To access the URL listed within parentheses, you must connect to the internet. The URL is provided to access outside of your air-gapped environment. 

## TranslationService

Provides natural language translation operations.

TranslateDocument  
---  
` rpc TranslateDocument(`[TranslateDocumentRequest](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.cloud.translation.v3#google.cloud.translation.v3.TranslateDocumentRequest)`) returns (`[TranslateDocumentResponse](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.cloud.translation.v3#google.cloud.translation.v3.TranslateDocumentResponse)`) ` Translates documents in synchronous mode.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-translation`
  * `https://www.googleapis.com/auth/cloud-platform`

  
  
## TranslateDocumentRequest

A document translation request.

Fields  
---  
`parent` |  `string` Required. Location to make a regional call.Format: `projects/{project-number-or-id}/locations/{location-id}`.For global calls, use `projects/{project-number-or-id}/locations/global` or `projects/{project-number-or-id}`.Non-global location is required for requests using AutoML models or custom glossaries.Models and glossaries must be within the same region (have the same location-id), otherwise an INVALID_ARGUMENT (400) error is returned.  
`source_language_code` |  `string` Optional. The ISO-639 language code of the input document if known, for example, "en-US" or "sr-Latn". Supported language codes are listed in Language Support. If the source language isn't specified, the API attempts to identify the source language automatically and returns the source language within the response. Source language must be specified if the request contains a glossary or a custom model.  
`target_language_code` |  `string` Required. The ISO-639 language code to use for translation of the input document, set to one of the language codes listed in Language Support.  
`document_input_config` |  ``[DocumentInputConfig](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects.locations/translateDocument#documentinputconfig)`` Required. Input configurations.  
`glossary_config` |  ``[TranslateTextGlossaryConfig](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.cloud.translation.v3#google.cloud.translation.v3.TranslateTextGlossaryConfig)`` Optional. Glossary to be applied. The glossary must be within the same region (have the same location-id) as the model, otherwise an INVALID_ARGUMENT (400) error is returned. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `glossaryConfig`:

  * `cloudtranslate.glossaries.docPredict`

  
  
## TranslateDocumentResponse

A translated document response message.

Fields  
---  
`document_translation` |  ``[DocumentTranslation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects.locations/translateDocument#documenttranslation)`` Translated document.  
`glossary_document_translation` |  ``[DocumentTranslation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects.locations/translateDocument#documenttranslation)`` The document's translation output if a glossary is provided in the request. This can be the same as [TranslateDocumentResponse.document_translation] if no glossary terms apply.  
`glossary_config` |  ``[TranslateTextGlossaryConfig](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.cloud.translation.v3#google.cloud.translation.v3.TranslateTextGlossaryConfig)`` The `glossary_config` used for this translation.  
CreateGlossary  
---  
` rpc CreateGlossary(`[CreateGlossaryRequest](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.cloud.translation.v3#google.cloud.translation.v3.CreateGlossaryRequest)`) returns (`[Operation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.longrunning#google.longrunning.Operation)`) ` Creates a glossary and returns the long-running operation. Returns NOT_FOUND, if the project doesn't exist.  
DeleteGlossary  
---  
` rpc DeleteGlossary(`[DeleteGlossaryRequest](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.cloud.translation.v3#google.cloud.translation.v3.DeleteGlossaryRequest)`) returns (`[Operation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.longrunning#google.longrunning.Operation)`) ` Deletes a glossary if the glossary hasn't been created. Returns NOT_FOUND, if the glossary doesn't exist.  
DetectLanguage  
---  
` rpc DetectLanguage(`[DetectLanguageRequest](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.cloud.translation.v3#google.cloud.translation.v3.DetectLanguageRequest)`) returns (`[DetectLanguageResponse](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.cloud.translation.v3#google.cloud.translation.v3.DetectLanguageResponse)`) ` Detects the language of text within a request.  
GetGlossary  
---  
` rpc GetGlossary(`[GetGlossaryRequest](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.cloud.translation.v3#google.cloud.translation.v3.GetGlossaryRequest)`) returns (`[Glossary](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.cloud.translation.v3#google.cloud.translation.v3.Glossary)`) ` Gets a glossary. Returns NOT_FOUND, if the glossary doesn't exist.  
GetSupportedLanguages  
---  
` rpc GetSupportedLanguages(`[GetSupportedLanguagesRequest](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.cloud.translation.v3#google.cloud.translation.v3.GetSupportedLanguagesRequest)`) returns (`[SupportedLanguages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.cloud.translation.v3#google.cloud.translation.v3.SupportedLanguages)`) ` Returns a list of supported languages for translation.  
ListGlossaries  
---  
` rpc ListGlossaries(`[ListGlossariesRequest](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.cloud.translation.v3#google.cloud.translation.v3.ListGlossariesRequest)`) returns (`[ListGlossariesResponse](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.cloud.translation.v3#google.cloud.translation.v3.ListGlossariesResponse)`) ` Lists glossaries in a project. Returns NOT_FOUND, if the project doesn't exist.  
TranslateText  
---  
` rpc TranslateText(`[TranslateTextRequest](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.cloud.translation.v3#google.cloud.translation.v3.TranslateTextRequest)`) returns (`[TranslateTextResponse](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.cloud.translation.v3#google.cloud.translation.v3.TranslateTextResponse)`) ` Translates input text and returns translated text.  
  
## CreateGlossaryMetadata

Stored in the `[google.longrunning.Operation.metadata](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.longrunning#google.longrunning.Operation.FIELDS.google.protobuf.Any.google.longrunning.Operation.metadata)` field returned by CreateGlossary.

Fields  
---  
`name` |  `string` The name of the glossary that is being created.  
`state` |  ``[State](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.cloud.translation.v3#google.cloud.translation.v3.CreateGlossaryMetadata.State)`` The current state of the glossary creation operation.  
`submit_time` |  ``[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)`` The time when the operation was submitted to the server.  
  
## State

Enumerates the possible states that the creation request can be in.

Enums  
---  
`STATE_UNSPECIFIED` | Invalid.  
`RUNNING` | Request is being processed.  
`SUCCEEDED` | The glossary was successfully created.  
`FAILED` | Failed to create the glossary.  
  
## CreateGlossaryRequest

Request message for CreateGlossary.

Fields  
---  
`parent` |  `string` Required. The project name.  
`glossary` |  ``[Glossary](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.cloud.translation.v3#google.cloud.translation.v3.Glossary)`` Required. The glossary to create.  
  
## DeleteGlossaryMetadata

Stored in the `[google.longrunning.Operation.metadata](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.longrunning#google.longrunning.Operation.FIELDS.google.protobuf.Any.google.longrunning.Operation.metadata)` field returned by DeleteGlossary.

Fields  
---  
`name` |  `string` The name of the glossary that is being deleted.  
`state` |  ``[State](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.cloud.translation.v3#google.cloud.translation.v3.DeleteGlossaryMetadata.State)`` The current state of the glossary deletion operation.  
`submit_time` |  ``[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)`` The time when the operation was submitted to the server.  
  
## State

Enumerates the possible states that the creation request can be in.

Enums  
---  
`STATE_UNSPECIFIED` | Invalid.  
`RUNNING` | Request is being processed.  
`SUCCEEDED` | The glossary was successfully deleted.  
`FAILED` | Failed to delete the glossary.  
  
## DeleteGlossaryRequest

Request message for DeleteGlossary.

Fields  
---  
`name` |  `string` Required. The name of the glossary to delete.  
  
## DeleteGlossaryResponse

Stored in the `[google.longrunning.Operation.response](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.longrunning#google.longrunning.Operation.FIELDS.google.protobuf.Any.google.longrunning.Operation.response)` field returned by DeleteGlossary.

Fields  
---  
`name` |  `string` The name of the deleted glossary.  
`submit_time` |  ``[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)`` The time when the operation was submitted to the server.  
`end_time` |  ``[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)`` The time when the glossary deletion is finished and `[google.longrunning.Operation.done](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.longrunning#google.longrunning.Operation.FIELDS.bool.google.longrunning.Operation.done)` is set to true.  
  
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
`languages[]` |  ``[DetectedLanguage](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.cloud.translation.v3#google.cloud.translation.v3.DetectedLanguage)`` The most probable language detected by the Translation API. For each request, the Translation API will always return only one result.  
  
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
  
## GetGlossaryRequest

Request message for GetGlossary.

Fields  
---  
`name` |  `string` Required. The name of the glossary to retrieve.  
  
## GetSupportedLanguagesRequest

The request message for discovering supported languages.

Fields  
---  
`parent` |  `string` Required. Project to make a call. Must refer to a caller's project.Format: `projects/{project-id}`.  
`display_language_code` |  `string` Optional. The language to use to return localized, human-readable names of supported languages. If missing, then display names aren't returned in a response.  
  
## Glossary

Represents a glossary built from user provided data.

Fields  
---  
`name` |  `string` Required. The resource name of the glossary. Glossary names have the form `projects/{project-id}/glossaries/{glossary-id}`.  
`input_config` |  ``[GlossaryInputConfig](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.cloud.translation.v3#google.cloud.translation.v3.GlossaryInputConfig)`` Required. Provides examples to build the glossary from. Total glossary must not exceed 10M Unicode codepoints.  
`entry_count` |  `int32` Output only. The number of entries defined in the glossary.  
`submit_time` |  ``[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)`` Output only. When CreateGlossary was called.  
`end_time` |  ``[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)`` Output only. When the glossary creation was finished.  
`display_name` |  `string` Optional. The display name of the glossary.  
Union field `languages`. Languages supported by the glossary. `languages` can be only one of the following:  
`language_pair` |  ``[LanguageCodePair](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.cloud.translation.v3#google.cloud.translation.v3.Glossary.LanguageCodePair)`` Used with unidirectional glossaries.  
`language_codes_set` |  ``[LanguageCodesSet](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.cloud.translation.v3#google.cloud.translation.v3.Glossary.LanguageCodesSet)`` Used with equivalent term set glossaries.  
  
## LanguageCodePair

Used with unidirectional glossaries.

Fields  
---  
`source_language_code` |  `string` Required. The BCP-47 language code of the input text, for example, "en-US". Expected to be an exact match for GlossaryTerm.language_code.  
`target_language_code` |  `string` Required. The BCP-47 language code for translation output, for example, "zh-CN". Expected to be an exact match for GlossaryTerm.language_code.  
  
## LanguageCodesSet

Used with equivalent term set glossaries.

Fields  
---  
`language_codes[]` |  `string` The BCP-47 language code(s) for terms defined in the glossary. All entries are unique. The list contains at least two entries. Expected to be an exact match for GlossaryTerm.language_code.  
  
## GlossaryInputConfig

Input configuration for glossaries.

Fields  
---  
`s3_source` |  ``[S3Source](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.cloud.translation.v3#google.cloud.translation.v3.GcsSource)`` Required. Storage location of glossary data. File format is determined based on the filename extension. API returns `[google.rpc.Code.INVALID_ARGUMENT](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.rpc#google.rpc.Code.ENUM_VALUES.google.rpc.Code.INVALID_ARGUMENT)` for unsupported URI-s and file formats. Wildcards aren't allowed. This must be a single file in one of the following formats:For unidirectional glossaries:

  * TSV/CSV (`.tsv`/`.csv`): 2 column file, tab- or comma-separated. The first column is source text. The second column is target text. The file must not contain headers. That is, the first row is data, not column names.
  * TMX (`.tmx`): TMX file with parallel data defining source/target term pairs.

For equivalent term sets glossaries:

  * CSV (`.csv`): Multi-column CSV file defining equivalent glossary terms in multiple languages. See documentation for more information - [glossaries](https://cloud.google.com/translate/docs/advanced/glossary).

  
  
## ListGlossariesRequest

Request message for ListGlossaries.

Fields  
---  
`parent` |  `string` Required. The name of the project from which to list all of the glossaries.  
`page_size` |  `int32` Optional. Requested page size. The server may return fewer glossaries than requested. If unspecified, the server picks an appropriate default.  
`page_token` |  `string` Optional. A token identifying a page of results the server should return. Typically, this is the value of [ListGlossariesResponse.next_page_token] returned from the previous call to `ListGlossaries` method. The first page is returned if `page_token` is empty or missing.  
`filter` |  `string` Optional. Filter specifying constraints of a list operation. Specify the constraint by the format of "key=value", where key must be "src" or "tgt", and the value must be a valid language code. For multiple restrictions, concatenate them by "AND" (uppercase only), such as: "src=en-US AND tgt=zh-CN". Notice that the exact match is used here, which means using 'en-US' and 'en' can lead to different results, which depends on the language code you used when you create the glossary. For the unidirectional glossaries, the "src" and "tgt" add restrictions on the source and target language code separately. For the equivalent term set glossaries, the "src" and/or "tgt" add restrictions on the term set. For example: "src=en-US AND tgt=zh-CN" will only pick the unidirectional glossaries which exactly match the source language code as "en-US" and the target language code "zh-CN", but all equivalent term set glossaries which contain "en-US" and "zh-CN" in their language set is picked. If missing, no filtering is performed.  
  
## ListGlossariesResponse

Response message for ListGlossaries.

Fields  
---  
`glossaries[]` |  ``[Glossary](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.cloud.translation.v3#google.cloud.translation.v3.Glossary)`` The list of glossaries for a project.  
`next_page_token` |  `string` A token to retrieve a page of results. Pass this value in the [ListGlossariesRequest.page_token] field in the subsequent call to `ListGlossaries` method to retrieve the next page of results.  
  
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
`languages[]` |  ``[SupportedLanguage](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.cloud.translation.v3#google.cloud.translation.v3.SupportedLanguage)`` A list of supported language responses. This list contains an entry for each language the Translation API supports.  
  
## TranslateTextGlossaryConfig

Configures which glossary should be used for a specific target language, and defines options for applying that glossary.

Fields  
---  
`glossary` |  `string` Required. The `glossary` to be applied for this translation.The format depends on glossary:

  * User provided custom glossary: `projects/{project-id}/glossaries/{glossary-id}`

  
`ignore_case` |  `bool` Optional. Indicates match is case-insensitive. Default value is false if missing.  
  
## TranslateTextRequest

The request message for synchronous translation.

Fields  
---  
`contents[]` |  `string` Required. The content of the input in string format. We recommend the total content be less than 30k codepoints. The max length of this field is 1024. Use BatchTranslateText for larger text.  
`mime_type` |  `string` Optional. The format of the source text, for example, "text/html", "text/plain". If left blank, the MIME type defaults to "text/html".  
`source_language_code` |  `string` The BCP-47 language code of the input text if known, for example, `en-US` or `sr-Latn`. Supported language codes are listed in Language Support.  
`target_language_code` |  `string` Required. The BCP-47 language code to use for translation of the input text, set to one of the language codes listed in Language Support.  
`parent` |  `string` Required. Project to make a call. Must refer to a caller's project.Format: `projects/{project-id}`  
`glossary_config` |  ``[TranslateTextGlossaryConfig](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.cloud.translation.v3#google.cloud.translation.v3.TranslateTextGlossaryConfig)`` Optional. Glossary to be applied.  
  
## TranslateTextResponse

Fields  
---  
`translations[]` |  ``[Translation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.cloud.translation.v3#google.cloud.translation.v3.Translation)`` Text translation responses with no glossary applied. This field has the same length as `[`contents`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.cloud.translation.v3#google.cloud.translation.v3.TranslateTextRequest.FIELDS.repeated.string.google.cloud.translation.v3.TranslateTextRequest.contents)`.  
`glossary_translations[]` |  ``[Translation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.cloud.translation.v3#google.cloud.translation.v3.Translation)`` Text translation responses if a glossary is provided in the request. This can be the same as `[`translations`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.cloud.translation.v3#google.cloud.translation.v3.TranslateTextResponse.FIELDS.repeated.google.cloud.translation.v3.Translation.google.cloud.translation.v3.TranslateTextResponse.translations)` if no terms apply. This field has the same length as `[`contents`](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.cloud.translation.v3#google.cloud.translation.v3.TranslateTextRequest.FIELDS.repeated.string.google.cloud.translation.v3.TranslateTextRequest.contents)`.  
  
## Translation

A single translation response.

Fields  
---  
`translated_text` |  `string` Text translated into the target language. If an error occurs during translation, this field might be excluded from the response.  
`detected_language_code` |  `string` If the source language was passed, auto-detection of the language doesn't occur and this field is empty.  
`glossary_config` |  ``[TranslateTextGlossaryConfig](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.cloud.translation.v3#google.cloud.translation.v3.TranslateTextGlossaryConfig)`` The `glossary_config` used for this translation.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-10 UTC."],[],[]] 
