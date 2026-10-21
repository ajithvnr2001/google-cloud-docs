---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateFileRequest/
title: AnnotateFileRequest \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:13:40.758504+00:00
---

# AnnotateFileRequest  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/AnnotateFileRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  AnnotateFileRequest Stay organized with collections  Save and categorize content based on your preferences. 

A request to annotate one single file, e.g. a PDF, TIFF or GIF file.

JSON representation  
---  
      
    
    {
      "inputConfig": {
        object ([InputConfig](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/InputConfig))
      },
      "features": [
        {
          object ([Feature](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/Feature))
        }
      ],
      "imageContext": {
        object ([ImageContext](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/ImageContext))
      },
      "pages": [
        integer
      ]
    }  
  
Fields  
---  
`inputConfig` |  `object (`[InputConfig](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/InputConfig)`)` Required. Information about the input file.  
`features[]` |  `object (`[Feature](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/Feature)`)` Required. Requested features.  
`imageContext` |  `object (`[ImageContext](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/ocr/rest/v1/ImageContext)`)` Additional context that may accompany the image(s) in the file.  
`pages[]` |  `integer` Pages of the file to perform image annotation.Pages starts from 1, we assume the first page of the file is page 1. At most 5 pages are supported per request. Pages can be negative.Page 1 means the first page. Page 2 means the second page. Page -1 means the last page. Page -2 means the second to the last page.If the file is GIF instead of PDF or TIFF, page refers to GIF frames.If this field is empty, by default the service performs image annotation for the first 5 pages of the file.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-10 UTC."],[],[]] 
