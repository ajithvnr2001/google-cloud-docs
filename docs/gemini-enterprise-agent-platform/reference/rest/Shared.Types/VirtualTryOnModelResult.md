---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VirtualTryOnModelResult/
title: VirtualTryOnModelResult \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T10:10:34.387545+00:00
---

# VirtualTryOnModelResult  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VirtualTryOnModelResult/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  VirtualTryOnModelResult Stay organized with collections  Save and categorize content based on your preferences. 

Represents the output of a Virtual Try-On prediction.

Fields  
  
`images[]` `object (`[Image](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VirtualTryOnModelResult#Image)`)` A list of generated images. The number of images returned is equal to the `sampleCount` parameter provided in the request. | JSON representation  
---  
      
    
    {
      "images": [
        {
          object ([Image](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VirtualTryOnModelResult#Image))
        }
      ]
    }  
  
## Image

Contains a generated image or information about why the image was filtered out.

Fields  
  
`mimeType` `string` The MIME type of the generated image.Supported values are: * `image/png` * `image/jpeg` | `data` `Union type`  
  
The generated image data or filtering reason. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`bytesBase64Encoded` `string` The generated image encoded as a base64 encoded bytes string. | `gcsUri` `string` The Google Cloud Storage URI where the generated image is stored. | `raiFilteredReason` `string` The reason why the generated image was filtered out by Responsible AI checks. If this field is present, no image is returned. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
      "mimeType": string,
    
      // data
      "bytesBase64Encoded": string,
      "gcsUri": string,
      "raiFilteredReason": string
      // Union type
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
