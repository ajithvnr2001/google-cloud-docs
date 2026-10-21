---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects.locations/translateDocument/
title: Method: projects.locations.translateDocument \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:13:48.210853+00:00
---

# Method: projects.locations.translateDocument  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects.locations/translateDocument/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  Method: projects.locations.translateDocument Stay organized with collections  Save and categorize content based on your preferences. 

Translates documents in synchronous mode.

### HTTP request

`POST https://{TRANSLATION_GDC_ENDPOINT}/v3/{parent}:translateDocument`

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
        object ([DocumentInputConfig](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects.locations/translateDocument#DocumentInputConfig))
      },
      "glossaryConfig": {
        object ([TranslateTextGlossaryConfig](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/TranslateTextGlossaryConfig))
      }
    }  
  
Fields  
---  
`sourceLanguageCode` |  `string` Optional. The ISO-639 language code of the input document if known, for example, "en-US" or "sr-Latn". Supported language codes are listed in Language Support. If the source language isn't specified, the API attempts to identify the source language automatically and returns the source language within the response. Source language must be specified if the request contains a glossary or a custom model.  
`targetLanguageCode` |  `string` Required. The ISO-639 language code to use for translation of the input document, set to one of the language codes listed in Language Support.  
`documentInputConfig` |  `object (`[DocumentInputConfig](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects.locations/translateDocument#DocumentInputConfig)`)` Required. Input configurations.  
`glossaryConfig` |  `object (`[TranslateTextGlossaryConfig](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/TranslateTextGlossaryConfig)`)` Optional. Glossary to be applied. The glossary must be within the same region (have the same location-id) as the model, otherwise an INVALID_ARGUMENT (400) error is returned. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `glossaryConfig`:

  * `cloudtranslate.glossaries.docPredict`

  
  
### Response body

A translated document response message.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "documentTranslation": {
        object ([DocumentTranslation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects.locations/translateDocument#DocumentTranslation))
      },
      "glossaryDocumentTranslation": {
        object ([DocumentTranslation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects.locations/translateDocument#DocumentTranslation))
      },
      "glossaryConfig": {
        object ([TranslateTextGlossaryConfig](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/TranslateTextGlossaryConfig))
      }
    }  
  
Fields  
---  
`documentTranslation` |  `object (`[DocumentTranslation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects.locations/translateDocument#DocumentTranslation)`)` Translated document.  
`glossaryDocumentTranslation` |  `object (`[DocumentTranslation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects.locations/translateDocument#DocumentTranslation)`)` The document's translation output if a glossary is provided in the request. This can be the same as [TranslateDocumentResponse.document_translation] if no glossary terms apply.  
`glossaryConfig` |  `object (`[TranslateTextGlossaryConfig](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/TranslateTextGlossaryConfig)`)` The `glossaryConfig` used for this translation.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-translation`
  * `https://www.googleapis.com/auth/cloud-platform`



## DocumentInputConfig

A document translation request input config.

JSON representation  
---  
      
    
    {
      "mimeType": string,
      "content": string,
      "S3Source": {
        object ([S3Source](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects.locations/translateDocument#DocumentInputConfig.FIELDS.s3_source))
      }
    }  
  
Fields  
---  
`mimeType` |  `string` Specifies the input document's mimeType.If not specified it will be determined using the file extension for S3Source provided files. For a file provided through bytes content the mimeType must be provided.Currently supported mime types are: 

  * application/pdf
  * application/msword
  * application/vnd.openxmlformats-officedocument.wordprocessingml.document
  * application/vnd.ms-powerpoint
  * application/vnd.openxmlformats-officedocument.presentationml.presentation
  * application/vnd.ms-excel
  * application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

Supported file formats are:

  * PDF
  * DOC
  * DOCX
  * PPT
  * PPTX
  * XLS
  * XLSX

  
`content` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Document's content represented as a stream of bytes.A base64-encoded string.  
`S3Source` |  `object (`[S3Source](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.cloud.translation.v3#s3source)`)` The storage location for the input content.  
  
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

Last updated 2026-04-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-10 UTC."],[],[]] 
