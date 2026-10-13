---
url: https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p3beta1.types.Symbol
title: Class Symbol (3.16.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:01:19.209701+00:00
---

# Class Symbol (3.16.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p3beta1.types.Symbol

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Symbol (3.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.16.0 (latest)  3.15.0  3.14.0  3.13.0  3.12.1  3.11.0  3.10.2  3.9.0  3.8.1  3.7.4  3.6.0  3.5.0  3.4.5  3.3.1  3.2.0  3.1.4  3.0.0  2.8.0  2.7.3  2.6.3  2.5.0  2.4.4  2.3.2  2.2.0  2.1.0  2.0.0  1.0.2  0.42.0  0.41.0  0.40.0  0.39.0  0.38.1 
    
    
    Symbol(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A single symbol representation.

## Attributes  
  
---  
**Name** | **Description**  
`property` |  `[google.cloud.vision_v1p3beta1.types.TextAnnotation.TextProperty](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p3beta1.types.TextAnnotation.TextProperty)`   
Additional information detected for the symbol.   
`bounding_box` |  `[google.cloud.vision_v1p3beta1.types.BoundingPoly](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1p3beta1.types.BoundingPoly)`   
The bounding box for the symbol. The vertices are in the order of top-left, top-right, bottom-right, bottom-left. When a rotation of the bounding box is detected the rotation is represented as around the top-left corner as defined when the text is read in the 'natural' orientation. For example: \- when the text is horizontal it might look like: 0----1 \| \| 3----2 \- when it's rotated 180 degrees around the top-left corner it becomes: 2----3 \| \| 1----0 and the vertice order will still be (0, 1, 2, 3).   
`text` |  `str`   
The actual UTF-8 representation of the symbol.   
`confidence` |  `float`   
Confidence of the OCR results for the symbol. Range [0, 1].   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
