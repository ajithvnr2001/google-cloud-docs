---
url: https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.ImageContext
title: Class ImageContext (3.16.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:52:26.174032+00:00
---

# Class ImageContext (3.16.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.ImageContext

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ImageContext (3.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.16.0 (latest)  3.15.0  3.14.0  3.13.0  3.12.1  3.11.0  3.10.2  3.9.0  3.8.1  3.7.4  3.6.0  3.5.0  3.4.5  3.3.1  3.2.0  3.1.4  3.0.0  2.8.0  2.7.3  2.6.3  2.5.0  2.4.4  2.3.2  2.2.0  2.1.0  2.0.0  1.0.2  0.42.0  0.41.0  0.40.0  0.39.0  0.38.1 
    
    
    ImageContext(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Image context and/or feature-specific parameters.

## Attributes  
  
---  
**Name** | **Description**  
`lat_long_rect` |  `[google.cloud.vision_v1p4beta1.types.LatLongRect](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.LatLongRect)`   
Not used.   
`language_hints` |  `MutableSequence[str]`   
List of languages to use for TEXT_DETECTION. In most cases, an empty value yields the best results since it enables automatic language detection. For languages based on the Latin alphabet, setting `language_hints` is not needed. In rare cases, when the language of the text in the image is known, setting a hint will help get better results (although it will be a significant hindrance if the hint is wrong). Text detection returns an error if one or more of the specified languages is not one of the `supported languages   
`crop_hints_params` |  `[google.cloud.vision_v1p4beta1.types.CropHintsParams](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.CropHintsParams)`   
Parameters for crop hints annotation request.   
`face_recognition_params` |  `[google.cloud.vision_v1p4beta1.types.FaceRecognitionParams](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.FaceRecognitionParams)`   
Parameters for face recognition.   
`product_search_params` |  `[google.cloud.vision_v1p4beta1.types.ProductSearchParams](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.ProductSearchParams)`   
Parameters for product search.   
`web_detection_params` |  `[google.cloud.vision_v1p4beta1.types.WebDetectionParams](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.WebDetectionParams)`   
Parameters for web detection.   
`text_detection_params` |  `[google.cloud.vision_v1p4beta1.types.TextDetectionParams](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p4beta1.types.TextDetectionParams)`   
Parameters for text detection and document text detection.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
