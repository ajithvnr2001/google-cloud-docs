---
url: https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.AnnotateVideoProgress
title: Class AnnotateVideoProgress (2.21.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:57:56.292269+00:00
---

# Class AnnotateVideoProgress (2.21.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.AnnotateVideoProgress

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AnnotateVideoProgress (2.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.21.0 (latest)  2.20.0  2.19.0  2.18.0  2.17.0  2.16.2  2.15.0  2.14.1  2.13.5  2.12.0  2.11.4  2.10.1  2.9.0  2.8.3  2.7.1  2.6.1  2.5.1  2.4.0  2.3.3  2.2.0  2.1.0  2.0.0  1.16.3  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.10.0 
    
    
    AnnotateVideoProgress(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Video annotation progress. Included in the `metadata` field of the `Operation` returned by the `GetOperation` call of the `google::longrunning::Operations` service.

## Attribute  
  
---  
**Name** | **Description**  
`annotation_progress` |  `MutableSequence[[google.cloud.videointelligence_v1.types.VideoAnnotationProgress](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.VideoAnnotationProgress)]`   
Progress metadata for all videos specified in `AnnotateVideoRequest`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
