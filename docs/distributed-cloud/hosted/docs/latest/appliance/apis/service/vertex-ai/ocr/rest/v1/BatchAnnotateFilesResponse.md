---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rest/v1/BatchAnnotateFilesResponse/
title: BatchAnnotateFilesResponse \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:16:08.562511+00:00
---

# BatchAnnotateFilesResponse  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rest/v1/BatchAnnotateFilesResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/reference/reference-overview)



Send feedback 

#  BatchAnnotateFilesResponse Stay organized with collections  Save and categorize content based on your preferences. 

A list of file annotation responses.

JSON representation  
---  
      
    
    {
      "responses": [
        {
          object ([AnnotateFileResponse](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rest/v1/BatchAnnotateFilesResponse#AnnotateFileResponse))
        }
      ]
    }  
  
Fields  
---  
`responses[]` |  `object (`[AnnotateFileResponse](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rest/v1/BatchAnnotateFilesResponse#AnnotateFileResponse)`)` The list of file annotation responses, each response corresponding to each AnnotateFileRequest in BatchAnnotateFilesRequest.  
  
## AnnotateFileResponse

Response to a single file annotation request. A file may contain one or more images, which individually have their own responses.

JSON representation  
---  
      
    
    {
      "inputConfig": {
        object ([InputConfig](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rest/v1/InputConfig))
      },
      "responses": [
        {
          object ([AnnotateImageResponse](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rest/v1/AnnotateImageResponse))
        }
      ],
      "totalPages": integer,
      "error": {
        object ([Status](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rest/v1/Status))
      }
    }  
  
Fields  
---  
`inputConfig` |  `object (`[InputConfig](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rest/v1/InputConfig)`)` Information about the file for which this response is generated.  
`responses[]` |  `object (`[AnnotateImageResponse](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rest/v1/AnnotateImageResponse)`)` Individual responses to images found within the file. This field will be empty if the `error` field is set.  
`totalPages` |  `integer` This field gives the total number of pages in the file.  
`error` |  `object (`[Status](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rest/v1/Status)`)` If set, represents the error message for the failed request. The `responses` field will not be set in this case.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-11 UTC."],[],[]] 
