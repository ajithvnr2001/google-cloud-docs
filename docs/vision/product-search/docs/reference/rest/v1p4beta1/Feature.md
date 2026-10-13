---
url: https://docs.cloud.google.com/vision/product-search/docs/reference/rest/v1p4beta1/Feature/
title: Feature \u00a0|\u00a0 Vision API Product Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:46:59.504684+00:00
---

# Feature  |  Vision API Product Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/product-search/docs/reference/rest/v1p4beta1/Feature/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Vision API Product Search ](https://docs.cloud.google.com/vision/product-search)
  * [ Reference ](https://docs.cloud.google.com/vision/product-search/docs/apis)



#  Feature Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Type



The type of Google Cloud Vision API detection to perform, and the maximum number of results to return for that type. Multiple `Feature` objects can be specified in the `features` list.

JSON representation  
---  
      
    
    {
      "type": enum ([Type](https://docs.cloud.google.com/vision/product-search/docs/reference/rest/v1p4beta1/Feature#Type)),
      "maxResults": number,
      "model": string
    }  
  
Fields  
---  
`type` |  `enum (`[Type](https://docs.cloud.google.com/vision/product-search/docs/reference/rest/v1p4beta1/Feature#Type)`)` The feature type.   
`maxResults` |  `number` Maximum number of results of this type. Does not apply to `TEXT_DETECTION`, `DOCUMENT_TEXT_DETECTION`, or `CROP_HINTS`.   
`model` |  `string` Model to use for the feature. Supported values: "builtin/stable" (the default if unset) and "builtin/latest".   
  
## Type

Type of Google Cloud Vision API feature to be extracted.

Enums  
---  
`TYPE_UNSPECIFIED` | Unspecified feature type.  
`FACE_DETECTION` | Run face detection.  
`LANDMARK_DETECTION` | Run landmark detection.  
`LOGO_DETECTION` | Run logo detection.  
`LABEL_DETECTION` | Run label detection.  
`TEXT_DETECTION` | Run text detection / optical character recognition (OCR). Text detection is optimized for areas of text within a larger image; if the image is a document, use `DOCUMENT_TEXT_DETECTION` instead.  
`DOCUMENT_TEXT_DETECTION` | Run dense text document OCR. Takes precedence when both `DOCUMENT_TEXT_DETECTION` and `TEXT_DETECTION` are present.  
`SAFE_SEARCH_DETECTION` | Run Safe Search to detect potentially unsafe or undesirable content.  
`IMAGE_PROPERTIES` | Compute a set of image properties, such as the image's dominant colors.  
`CROP_HINTS` | Run crop hints.  
`WEB_DETECTION` | Run web detection.  
`PRODUCT_SEARCH` | Run Product Search.  
`OBJECT_LOCALIZATION` | Run localizer for object detection.  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
