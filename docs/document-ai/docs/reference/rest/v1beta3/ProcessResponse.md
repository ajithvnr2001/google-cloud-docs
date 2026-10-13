---
url: https://docs.cloud.google.com/document-ai/docs/reference/rest/v1beta3/ProcessResponse/
title: ProcessResponse \u00a0|\u00a0 Document AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:22:05.289924+00:00
---

# ProcessResponse  |  Document AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-ai/docs/reference/rest/v1beta3/ProcessResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI ](https://docs.cloud.google.com/document-ai/docs)
  * [ Reference ](https://docs.cloud.google.com/document-ai/docs/reference)



Send feedback 

#  ProcessResponse Stay organized with collections  Save and categorize content based on your preferences. 

Response message for the `[ProcessDocument](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1beta3/projects.locations.processors/process#google.cloud.documentai.v1beta3.DocumentProcessorService.ProcessDocument)` method.

JSON representation  
---  
      
    
    {
      "document": {
        object ([Document](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1beta3/Document))
      },
      "humanReviewOperation": string,
      "humanReviewStatus": {
        object (HumanReviewStatus)
      }
    }  
  
Fields  
---  
`document` |  `object (`[Document](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1beta3/Document)`)` The document payload, will populate fields based on the processor's behavior.  
`humanReviewOperation  
**(deprecated)**` |  `string` This item is deprecated!The name of the operation triggered by the processed document. If the human review process isn't triggered, this field is empty. It has the same response type and metadata as the long-running operation returned by `[ReviewDocument](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1beta3/projects.locations.processors.humanReviewConfig/reviewDocument#google.cloud.documentai.v1beta3.DocumentProcessorService.ReviewDocument)`.  
`humanReviewStatus` |  `object (`HumanReviewStatus`)` The status of human review on the processed document.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
