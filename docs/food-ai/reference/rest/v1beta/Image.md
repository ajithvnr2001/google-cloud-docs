---
url: https://docs.cloud.google.com/food-ai/reference/rest/v1beta/Image/
title: Image \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T09:53:57.300881+00:00
---

# Image  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/food-ai/reference/rest/v1beta/Image/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Food AI ](https://docs.cloud.google.com/food-ai)



Send feedback 

#  Image Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * ImageSource
    * JSON representation



Image to display for a menu entity.

JSON representation  
---  
      
    
    {
      "sourceUri": string,
      "sources": [
        {
          object ([ImageSource](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/Image#ImageSource))
        }
      ]
    }  
  
Fields  
---  
`sourceUri` |  `string` Required. The source URI of the image.  
`sources[]` |  `object (`[ImageSource](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/Image#ImageSource)`)` Optional. The sources of the image with different resolutions.  
  
## ImageSource

Image uri with resolution.

JSON representation  
---  
      
    
    {
      "uri": string,
      "width": integer,
      "height": integer
    }  
  
Fields  
---  
`uri` |  `string` Optional. The URI of the image.  
`width` |  `integer` Optional. The width of the image.  
`height` |  `integer` Optional. The height of the image.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-21 UTC."],[],[]] 
