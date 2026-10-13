---
url: https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/documents/analyzeEntitySentiment/
title: Method: documents.analyzeEntitySentiment \u00a0|\u00a0 Cloud Natural Language API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:11:53.060118+00:00
---

# Method: documents.analyzeEntitySentiment  |  Cloud Natural Language API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/documents/analyzeEntitySentiment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Natural Language API ](https://docs.cloud.google.com/natural-language/docs)
  * [ Reference ](https://docs.cloud.google.com/natural-language/docs/apis)



Send feedback 

#  Method: documents.analyzeEntitySentiment Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Finds entities, similar to `[documents.analyzeEntities](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/documents/analyzeEntities#google.cloud.language.v1.LanguageService.AnalyzeEntities)` in the text and analyzes sentiment associated with each entity and its mentions.

### HTTP request

`POST https://language.googleapis.com/v1/documents:analyzeEntitySentiment`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "document": {
        object ([Document](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/documents#Document))
      },
      "encodingType": enum ([EncodingType](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/EncodingType))
    }  
  
Fields  
---  
`document` |  `object (`[Document](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/documents#Document)`)` Required. Input document.  
`encodingType` |  `enum (`[EncodingType](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/EncodingType)`)` The encoding type used by the API to calculate offsets.  
  
### Response body

The entity-level sentiment analysis response message.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "entities": [
        {
          object ([Entity](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/Entity))
        }
      ],
      "language": string
    }  
  
Fields  
---  
`entities[]` |  `object (`[Entity](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/Entity)`)` The recognized entities in the input document with associated sentiments.  
`language` |  `string` The language of the text, which will be the same as the language specified in the request or, if not specified, the automatically-detected language. See `[Document.language](https://docs.cloud.google.com/natural-language/docs/reference/rest/v1/documents#Document.FIELDS.language)` field for more details.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-language`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-13 UTC."],[],[]] 
