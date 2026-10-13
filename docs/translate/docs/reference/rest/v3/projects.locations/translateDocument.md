---
url: https://docs.cloud.google.com/translate/docs/reference/rest/v3/projects.locations/translateDocument/
title: Method: projects.locations.translateDocument \u00a0|\u00a0 Cloud Translation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:21:38.262507+00:00
---

# Method: projects.locations.translateDocument  |  Cloud Translation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/translate/docs/reference/rest/v3/projects.locations/translateDocument/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Translation ](https://docs.cloud.google.com/translate/docs)
  * [ API and references ](https://docs.cloud.google.com/translate/docs/reference/api-overview)



Send feedback 

#  Method: projects.locations.translateDocument Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * DocumentInputConfig
    * JSON representation
  * DocumentOutputConfig
    * JSON representation
  * DocumentTranslation
    * JSON representation
  * Try it!



Translates documents in synchronous mode.

### HTTP request

`POST https://translate.googleapis.com/v3/{parent=projects/*/locations/*}:translateDocument`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Location to make a regional call.Format: `projects/{project-number-or-id}/locations/{location-id}`.For global calls, use `projects/{project-number-or-id}/locations/global` or `projects/{project-number-or-id}`.Non-global location is required for requests using AutoML models or custom glossaries.Models and glossaries must be within the same region (have the same location-id), otherwise an INVALID_ARGUMENT (400) error is returned.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "sourceLanguageCode": string,
      "targetLanguageCode": string,
      "documentInputConfig": {
        object ([DocumentInputConfig](https://docs.cloud.google.com/translate/docs/reference/rest/v3/projects.locations/translateDocument#DocumentInputConfig))
      },
      "documentOutputConfig": {
        object ([DocumentOutputConfig](https://docs.cloud.google.com/translate/docs/reference/rest/v3/projects.locations/translateDocument#DocumentOutputConfig))
      },
      "model": string,
      "glossaryConfig": {
        object ([TranslateTextGlossaryConfig](https://docs.cloud.google.com/translate/docs/reference/rest/v3/TranslateTextGlossaryConfig))
      },
      "labels": {
        string: string,
        ...
      },
      "customizedAttribution": string,
      "isTranslateNativePdfOnly": boolean,
      "enableShadowRemovalNativePdf": boolean,
      "enableRotationCorrection": boolean
    }  
  
Fields  
---  
`sourceLanguageCode` |  `string` Optional. The ISO-639 language code of the input document if known, for example, "en-US" or "sr-Latn". Supported language codes are listed in [Language Support](https://cloud.google.com/translate/docs/languages). If the source language isn't specified, the API attempts to identify the source language automatically and returns the source language within the response. Source language must be specified if the request contains a glossary or a custom model.  
`targetLanguageCode` |  `string` Required. The ISO-639 language code to use for translation of the input document, set to one of the language codes listed in [Language Support](https://cloud.google.com/translate/docs/languages).  
`documentInputConfig` |  `object (`[DocumentInputConfig](https://docs.cloud.google.com/translate/docs/reference/rest/v3/projects.locations/translateDocument#DocumentInputConfig)`)` Required. Input configurations.  
`documentOutputConfig` |  `object (`[DocumentOutputConfig](https://docs.cloud.google.com/translate/docs/reference/rest/v3/projects.locations/translateDocument#DocumentOutputConfig)`)` Optional. Output configurations. Defines if the output file should be stored within Cloud Storage as well as the desired output format. If not provided the translated file will only be returned through a byte-stream and its output mime type will be the same as the input file's mime type.  
`model` |  `string` Optional. The `model` type requested for this translation.The format depends on model type:

  * AutoML Translation models: `projects/{project-number-or-id}/locations/{location-id}/models/{model-id}`
  * General (built-in) models: `projects/{project-number-or-id}/locations/{location-id}/models/general/nmt`,

If not provided, the default Google model (NMT) will be used for translation. Authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions on the specified resource `model`:

  * `cloudtranslate.generalModels.docPredict`
  * `automl.models.predict`

  
`glossaryConfig` |  `object (`[TranslateTextGlossaryConfig](https://docs.cloud.google.com/translate/docs/reference/rest/v3/TranslateTextGlossaryConfig)`)` Optional. Glossary to be applied. The glossary must be within the same region (have the same location-id) as the model, otherwise an INVALID_ARGUMENT (400) error is returned. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `glossaryConfig`:

  * `cloudtranslate.glossaries.docPredict`

  
`labels` |  `map (key: string, value: string)` Optional. The labels with user-defined metadata for the request.Label keys and values can be no longer than 63 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. Label values are optional. Label keys must start with a letter.See <https://cloud.google.com/translate/docs/advanced/labels> for more information.  
`customizedAttribution` |  `string` Optional. This flag is to support user customized attribution. If not provided, the default is `Machine Translated by Google`. Customized attribution should follow rules in <https://cloud.google.com/translate/attribution#attribution_and_logos>  
`isTranslateNativePdfOnly` |  `boolean` Optional. isTranslateNativePdfOnly field for external customers. If true, the page limit of online native pdf translation is 300 and only native pdf pages will be translated.  
`enableShadowRemovalNativePdf` |  `boolean` Optional. If true, use the text removal server to remove the shadow text on background image for native pdf translation. Shadow removal feature can only be enabled when isTranslateNativePdfOnly: false && pdfNativeOnly: false  
`enableRotationCorrection` |  `boolean` Optional. If true, enable auto rotation correction in DVS.  
  
### Response body

A translated document response message.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "documentTranslation": {
        object ([DocumentTranslation](https://docs.cloud.google.com/translate/docs/reference/rest/v3/projects.locations/translateDocument#DocumentTranslation))
      },
      "glossaryDocumentTranslation": {
        object ([DocumentTranslation](https://docs.cloud.google.com/translate/docs/reference/rest/v3/projects.locations/translateDocument#DocumentTranslation))
      },
      "model": string,
      "glossaryConfig": {
        object ([TranslateTextGlossaryConfig](https://docs.cloud.google.com/translate/docs/reference/rest/v3/TranslateTextGlossaryConfig))
      }
    }  
  
Fields  
---  
`documentTranslation` |  `object (`[DocumentTranslation](https://docs.cloud.google.com/translate/docs/reference/rest/v3/projects.locations/translateDocument#DocumentTranslation)`)` Translated document.  
`glossaryDocumentTranslation` |  `object (`[DocumentTranslation](https://docs.cloud.google.com/translate/docs/reference/rest/v3/projects.locations/translateDocument#DocumentTranslation)`)` The document's translation output if a glossary is provided in the request. This can be the same as [TranslateDocumentResponse.document_translation] if no glossary terms apply.  
`model` |  `string` Only present when 'model' is present in the request. 'model' is normalized to have a project number.For example: If the 'model' field in TranslateDocumentRequest is: `projects/{project-id}/locations/{location-id}/models/general/nmt` then `model` here would be normalized to `projects/{project-number}/locations/{location-id}/models/general/nmt`.  
`glossaryConfig` |  `object (`[TranslateTextGlossaryConfig](https://docs.cloud.google.com/translate/docs/reference/rest/v3/TranslateTextGlossaryConfig)`)` The `glossaryConfig` used for this translation.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-translation`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

## DocumentInputConfig

A document translation request input config.

JSON representation  
---  
      
    
    {
      "mimeType": string,
    
      // Union field source can be only one of the following:
      "content": string,
      "gcsSource": {
        object ([GcsSource](https://docs.cloud.google.com/translate/docs/reference/rest/v3/projects.locations.glossaries#GcsSource))
      }
      // End of list of possible types for union field source.
    }  
  
Fields  
---  
`mimeType` |  `string` Specifies the input document's mimeType.If not specified it will be determined using the file extension for gcsSource provided files. For a file provided through bytes content the mimeType must be provided. Currently supported mime types are: - application/pdf - application/vnd.openxmlformats-officedocument.wordprocessingml.document - application/vnd.openxmlformats-officedocument.presentationml.presentation - application/vnd.openxmlformats-officedocument.spreadsheetml.sheet  
Union field `source`. Specifies the source for the document's content. The input file size should be <= 20MB for - application/vnd.openxmlformats-officedocument.wordprocessingml.document - application/vnd.openxmlformats-officedocument.presentationml.presentation - application/vnd.openxmlformats-officedocument.spreadsheetml.sheet The input file size should be <= 20MB and the maximum page limit is 20 for - application/pdf `source` can be only one of the following:  
`content` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Document's content represented as a stream of bytes.A base64-encoded string.  
`gcsSource` |  `object (`[GcsSource](https://docs.cloud.google.com/translate/docs/reference/rest/v3/projects.locations.glossaries#GcsSource)`)` Google Cloud Storage location. This must be a single file. For example: <gs://example_bucket/example_file.pdf>  
  
## DocumentOutputConfig

A document translation request output config.

JSON representation  
---  
      
    
    {
      "mimeType": string,
    
      // Union field destination can be only one of the following:
      "gcsDestination": {
        object ([GcsDestination](https://docs.cloud.google.com/translate/docs/reference/rest/v3/GcsDestination))
      }
      // End of list of possible types for union field destination.
    }  
  
Fields  
---  
`mimeType` |  `string` Optional. Specifies the translated document's mimeType. If not specified, the translated file's mime type will be the same as the input file's mime type. Currently only support the output mime type to be the same as input mime type. - application/pdf - application/vnd.openxmlformats-officedocument.wordprocessingml.document - application/vnd.openxmlformats-officedocument.presentationml.presentation - application/vnd.openxmlformats-officedocument.spreadsheetml.sheet  
Union field `destination`. A URI destination for the translated document. It is optional to provide a destination. If provided the results from TranslateDocument will be stored in the destination. Whether a destination is provided or not, the translated documents will be returned within TranslateDocumentResponse.document_translation and TranslateDocumentResponse.glossary_document_translation. `destination` can be only one of the following:  
`gcsDestination` |  `object (`[GcsDestination](https://docs.cloud.google.com/translate/docs/reference/rest/v3/GcsDestination)`)` Optional. Google Cloud Storage destination for the translation output, e.g., `gs://my_bucket/my_directory/`.The destination directory provided does not have to be empty, but the bucket must exist. If a file with the same name as the output file already exists in the destination an error will be returned.For a DocumentInputConfig.contents provided document, the output file will have the name "output_[trg]_translations.[ext]", where - [trg] corresponds to the translated file's language code, - [ext] corresponds to the translated file's extension according to its mime type.For a DocumentInputConfig.gcs_uri provided document, the output file will have a name according to its URI. For example: an input file with URI: `gs://a/b/c.[extension]` stored in a gcsDestination bucket with name "my_bucket" will have an output URI: `gs://my_bucket/a_b_c_[trg]_translations.[ext]`, where - [trg] corresponds to the translated file's language code, - [ext] corresponds to the translated file's extension according to its mime type.If the document was directly provided through the request, then the output document will have the format: `gs://my_bucket/translated_document_[trg]_translations.[ext]`, where - [trg] corresponds to the translated file's language code, - [ext] corresponds to the translated file's extension according to its mime type.If a glossary was provided, then the output URI for the glossary translation will be equal to the default output URI but have `glossaryTranslations` instead of `translations`. For the previous example, its glossary URI would be: `gs://my_bucket/a_b_c_[trg]_glossary_translations.[ext]`.Thus the max number of output files will be 2 (Translated document, Glossary translated document).Callers should expect no partial outputs. If there is any error during document translation, no output will be stored in the Cloud Storage bucket.  
  
## DocumentTranslation

A translated document message.

JSON representation  
---  
      
    
    {
      "byteStreamOutputs": [
        string
      ],
      "mimeType": string,
      "detectedLanguageCode": string
    }  
  
Fields  
---  
`byteStreamOutputs[]` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` The array of translated documents. It is expected to be size 1 for now. We may produce multiple translated documents in the future for other type of file formats.A base64-encoded string.  
`mimeType` |  `string` The translated document's mime type.  
`detectedLanguageCode` |  `string` The detected language for the input document. If the user did not provide the source language for the input document, this field will have the language code automatically detected. If the source language was passed, auto-detection of the language does not occur and this field is empty.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-29 UTC."],[],[]] 
