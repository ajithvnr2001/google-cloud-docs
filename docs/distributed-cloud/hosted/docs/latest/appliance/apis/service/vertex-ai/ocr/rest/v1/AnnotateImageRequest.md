---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rest/v1/AnnotateImageRequest/
title: AnnotateImageRequest \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:16:07.925724+00:00
---

# AnnotateImageRequest  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rest/v1/AnnotateImageRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/reference/reference-overview)



Send feedback 

#  AnnotateImageRequest Stay organized with collections  Save and categorize content based on your preferences. 

Request for performing Google Cloud Vision API tasks over a user-provided image, with user-requested features, and with context information.

JSON representation  
---  
      
    
    {
      "image": {
        object ([Image](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rest/v1/AnnotateImageRequest#Image))
      },
      "features": [
        {
          object ([Feature](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rest/v1/Feature))
        }
      ],
      "imageContext": {
        object ([ImageContext](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rest/v1/ImageContext))
      }
    }  
  
Fields  
---  
`image` |  `object (`[Image](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rest/v1/AnnotateImageRequest#Image)`)` The image to be processed.  
`features[]` |  `object (`[Feature](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rest/v1/Feature)`)` Requested features.  
`imageContext` |  `object (`[ImageContext](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/vertex-ai/ocr/rest/v1/ImageContext)`)` Additional context that may accompany the image.  
  
## Image

Client image to perform Google Cloud Vision API tasks over.

JSON representation  
---  
      
    
    {
      "content": string
    }  
  
Fields  
---  
`content` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Image content, represented as a stream of bytes. Note: As with all `bytes` fields, protobuffers use a pure binary representation, whereas JSON representations use base64.Currently, this field only works for images.annotate requests.A base64-encoded string.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-11 UTC."],[],[]] 
