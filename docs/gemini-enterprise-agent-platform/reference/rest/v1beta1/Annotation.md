---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Annotation/
title: Annotation \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:03:36.084280+00:00
---

# Annotation  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Annotation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Annotation Stay organized with collections  Save and categorize content based on your preferences. 

Citation information for model-generated content.

Fields  
  
`startIndex` `integer` Start of segment of the response that is attributed to this source.Index indicates the start of the segment, measured in bytes. | `endIndex` `integer` End of the attributed segment, exclusive. | `type` `Union type`  
  
The type of annotation. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`urlCitation` `object (`[UrlCitation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Annotation#UrlCitation)`)` NOTE: We use these instead of the Citation message for historical reasons. A URL citation annotation. | `fileCitation` `object (`[FileCitation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Annotation#FileCitation)`)` A file citation annotation. | `placeCitation` `object (`[PlaceCitation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Annotation#PlaceCitation)`)` A place citation annotation. | `wordInfo` `object (`[WordInfo](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Annotation#WordInfo)`)` word-level ASR annotation with timing and speaker info. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
      "startIndex": integer,
      "endIndex": integer,
    
      // type
      "urlCitation": {
        object ([UrlCitation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Annotation#UrlCitation))
      },
      "fileCitation": {
        object ([FileCitation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Annotation#FileCitation))
      },
      "placeCitation": {
        object ([PlaceCitation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Annotation#PlaceCitation))
      },
      "wordInfo": {
        object ([WordInfo](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Annotation#WordInfo))
      }
      // Union type
    }  
  
## UrlCitation

A URL citation annotation.

Fields  
  
`url` `string` The URL. | `title` `string` The title of the URL. | JSON representation  
---  
      
    
    {
      "url": string,
      "title": string
    }  
  
## FileCitation

A file citation annotation.

Fields  
  
`documentUri` `string` The URI of the file. | `fileName` `string` The name of the file. | `source` `string` Source attributed for a portion of the text. | `customMetadata` `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` user provided metadata about the retrieved context. | `pageNumber` `integer` Page number of the cited document, if applicable. | `mediaId` `string` Media id in-case of image citations, if applicable. | JSON representation  
---  
      
    
    {
      "documentUri": string,
      "fileName": string,
      "source": string,
      "customMetadata": {
        object
      },
      "pageNumber": integer,
      "mediaId": string
    }  
  
## PlaceCitation

A place citation annotation.

Fields  
  
`placeId` `string` The id of the place, in `places/{placeId}` format. | `name` `string` title of the place. | `url` `string` URI reference of the place. | `reviewSnippets[]` `object (`[ReviewSnippet](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ReviewSnippet)`)` Snippets of reviews that are used to generate answers about the features of a given place in Google Maps. | JSON representation  
---  
      
    
    {
      "placeId": string,
      "name": string,
      "url": string,
      "reviewSnippets": [
        {
          object ([ReviewSnippet](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ReviewSnippet))
        }
      ]
    }  
  
## WordInfo

word-level ASR annotation for transcription output. Carries the word text, optional timing, and optional speaker attribution.

Fields  
  
`text` `string` The transcribed word. | `startOffset` `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Start offset in time of the word relative to the start of the audio. Present when timestampGranularities contains "word".A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`. | `endOffset` `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` End offset in time of the word relative to the start of the audio. Present when timestampGranularities contains "word".A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`. | `speaker` `string` Optional. Speaker label for this word (e.g. "spk_1", "spk_2"). Present when diarizationMode is set in TranscriptionConfig. | JSON representation  
---  
      
    
    {
      "text": string,
      "startOffset": string,
      "endOffset": string,
      "speaker": string
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
