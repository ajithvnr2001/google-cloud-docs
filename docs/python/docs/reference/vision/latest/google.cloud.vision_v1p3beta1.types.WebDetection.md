---
url: https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p3beta1.types.WebDetection
title: Class WebDetection (3.16.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:33:53.519133+00:00
---

# Class WebDetection (3.16.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p3beta1.types.WebDetection

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class WebDetection (3.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.16.0 (latest)  3.15.0  3.14.0  3.13.0  3.12.1  3.11.0  3.10.2  3.9.0  3.8.1  3.7.4  3.6.0  3.5.0  3.4.5  3.3.1  3.2.0  3.1.4  3.0.0  2.8.0  2.7.3  2.6.3  2.5.0  2.4.4  2.3.2  2.2.0  2.1.0  2.0.0  1.0.2  0.42.0  0.41.0  0.40.0  0.39.0  0.38.1 
    
    
    WebDetection(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Relevant information for the image from the Internet.

## Attributes  
  
---  
**Name** | **Description**  
`web_entities` |  `MutableSequence[[google.cloud.vision_v1p3beta1.types.WebDetection.WebEntity](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p3beta1.types.WebDetection.WebEntity)]`   
Deduced entities from similar images on the Internet.   
`full_matching_images` |  `MutableSequence[[google.cloud.vision_v1p3beta1.types.WebDetection.WebImage](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p3beta1.types.WebDetection.WebImage)]`   
Fully matching images from the Internet. Can include resized copies of the query image.   
`partial_matching_images` |  `MutableSequence[[google.cloud.vision_v1p3beta1.types.WebDetection.WebImage](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p3beta1.types.WebDetection.WebImage)]`   
Partial matching images from the Internet. Those images are similar enough to share some key-point features. For example an original image will likely have partial matching for its crops.   
`pages_with_matching_images` |  `MutableSequence[[google.cloud.vision_v1p3beta1.types.WebDetection.WebPage](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p3beta1.types.WebDetection.WebPage)]`   
Web pages containing the matching images from the Internet.   
`visually_similar_images` |  `MutableSequence[[google.cloud.vision_v1p3beta1.types.WebDetection.WebImage](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p3beta1.types.WebDetection.WebImage)]`   
The visually similar image results.   
`best_guess_labels` |  `MutableSequence[[google.cloud.vision_v1p3beta1.types.WebDetection.WebLabel](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p3beta1.types.WebDetection.WebLabel)]`   
Best guess text labels for the request image.   
  
## Classes 

### WebEntity
    
    
    WebEntity(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Entity deduced from similar images on the Internet.

### WebImage
    
    
    WebImage(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Metadata for online images.

### WebLabel
    
    
    WebLabel(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Label to provide extra metadata for the web detection.

### WebPage
    
    
    WebPage(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Metadata for web pages.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
