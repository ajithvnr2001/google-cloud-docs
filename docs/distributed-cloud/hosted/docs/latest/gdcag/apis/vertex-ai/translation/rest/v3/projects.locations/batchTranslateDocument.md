---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects.locations/batchTranslateDocument/
title: Method: projects.locations.batchTranslateDocument \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:13:46.697752+00:00
---

# Method: projects.locations.batchTranslateDocument  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects.locations/batchTranslateDocument/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  Method: projects.locations.batchTranslateDocument Stay organized with collections  Save and categorize content based on your preferences. 

Translates a large volume of document in asynchronous batch mode. This function provides real-time output as the inputs are being processed. If caller cancels a request, the partial results (for an input file, it's all or nothing) may still be available on the specified output location.

This call returns immediately and you can use google.longrunning.Operation.name to poll the status of the call.

### HTTP request

`POST https://{TRANSLATION_GDC_ENDPOINT}/v3/{parent}:batchTranslateDocument`

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Location to make a call.Format: `projects/{project-id}`.The `global` location is not supported for batch translation.Only glossaries within the same region (have the same location-id) can be used, otherwise an INVALID_ARGUMENT (400) error is returned.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "sourceLanguageCode": string,
      "targetLanguageCodes": [
        string
      ],
      "inputConfigs": [
        {
          object ([BatchDocumentInputConfig](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects.locations/batchTranslateDocument#BatchDocumentInputConfig))
        }
      ],
      "outputConfig": {
        object ([BatchDocumentOutputConfig](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects.locations/batchTranslateDocument#BatchDocumentOutputConfig))
      },
      "glossaries": {
        string: {
          object ([TranslateTextGlossaryConfig](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/TranslateTextGlossaryConfig))
        },
        ...
      },
      "formatConversions": {
        string: string,
        ...
      },
      "customizedAttribution": string,
      "enableShadowRemovalNativePdf": boolean,
      "enableRotationCorrection": boolean
    }  
  
Fields  
---  
`sourceLanguageCode` |  `string` Required. The ISO-639 language code of the input document if known, for example, "en-US" or "sr-Latn". Supported language codes are listed in [Supported languages](https://cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-translation#SupportedLanguages).  
`targetLanguageCodes[]` |  `string` Required. The ISO-639 language code to use for translation of the input document. Specify up to 10 language codes here.  
`inputConfigs[]` |  `object (`[BatchDocumentInputConfig](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects.locations/batchTranslateDocument#BatchDocumentInputConfig)`)` Required. Input configurations. The total number of files matched should be <= 100. The total content size to translate should be <= 100M Unicode codepoints. The files must use UTF-8 encoding.  
`outputConfig` |  `object (`[BatchDocumentOutputConfig](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects.locations/batchTranslateDocument#BatchDocumentOutputConfig)`)` Required. Output configuration. If 2 input configs match to the same file (that is, same input path), we don't generate output for duplicate inputs.  
`glossaries` |  `map (key: string, value: object (`[TranslateTextGlossaryConfig](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/TranslateTextGlossaryConfig)`))` Optional. Glossaries to be applied. It's keyed by target language code.  
`formatConversions` |  `map (key: string, value: string)` Optional. The file format conversion map that is applied to all input files. The map key is the original mimeType. The map value is the target mimeType of translated documents.Supported file format conversion includes: - `application/pdf` to `application/vnd.openxmlformats-officedocument.wordprocessingml.document`If nothing specified, output files will be in the same format as the original file.  
`customizedAttribution` |  `string` Optional. This flag is to support user customized attribution. If not provided, the default is `Machine Translated by Google`. Customized attribution should follow rules in <https://cloud.google.com/translate/attribution#attribution_and_logos>  
`enableShadowRemovalNativePdf` |  `boolean` Optional. If true, use the text removal server to remove the shadow text on background image for native pdf translation. Shadow removal feature can only be enabled when `isTranslateNativePdfOnly: false && pdfNativeOnly: false`  
`enableRotationCorrection` |  `boolean` Optional. If true, enable auto rotation correction in DVS.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rest/v3/projects.operations#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



## BatchDocumentInputConfig

Input configuration for locations.batchTranslateDocument request.

JSON representation  
---  
      
    
    {
    
      // Union field source can be only one of the following:
      "s3_source": {
        object (s3Source)
      }
      // End of list of possible types for union field source.
    }  
  
Fields  
---  
Union field `source`. Specify the input. `source` can be only one of the following:  
`s3_source` |  `object (`s3Source`)` S3 bucket location for the source input. This can be a single file or a wildcard.File mime type is determined based on extension. Supported mime type includes: 

  * `pdf`: application/pdf
  * `docx`: application/vnd.openxmlformats-officedocument.wordprocessingml.document
  * `pptx`: application/vnd.openxmlformats-officedocument.presentationml.presentation
  * `xlsx`: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

The max file size to support for `.docx`, `.pptx` and `.xlsx` is 100MB. The max file size to support for `.pdf` is 1GB and the max page limit is 1000 pages. The max file size to support for all input documents is 1GB.  
  
## BatchDocumentOutputConfig

Output configuration for locations.batchTranslateDocument request.

JSON representation  
---  
      
    
    {
    
      // Union field destination can be only one of the following:
      "s3_destination": {
        object (s3Destination)
      }
      // End of list of possible types for union field destination.
    }  
  
Fields  
---  
Union field `destination`. The destination of output. The destination directory provided must exist and be empty. `destination` can be only one of the following:  
`s3_destination` |  `object (`s3Destination`)` S3 bucket destination for output content. For every single input document, we generate at most 2 * n output files. (n is the number of target language codes in the `BatchTranslateDocumentRequest`).`targetLanguageCode` is provided in the request.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-10 UTC."],[],[]] 
