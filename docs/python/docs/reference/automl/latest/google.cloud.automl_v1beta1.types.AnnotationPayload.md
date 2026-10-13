---
url: https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.AnnotationPayload
title: Class AnnotationPayload (2.21.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:57:42.493294+00:00
---

# Class AnnotationPayload (2.21.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.AnnotationPayload

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AnnotationPayload (2.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.21.0 (latest)  2.20.1  2.19.0  2.18.1  2.17.0  2.16.4  2.15.0  2.14.1  2.13.5  2.12.0  2.11.4  2.10.1  2.9.0  2.8.3  2.7.3  2.6.0  2.5.2  2.4.2  2.3.0  2.2.0  2.1.0  2.0.0  1.0.3  0.10.0  0.9.0  0.8.0  0.7.1  0.6.0  0.5.0  0.4.0 
    
    
    AnnotationPayload(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Contains annotation information that is relevant to AutoML.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`translation` |  `[google.cloud.automl_v1beta1.types.TranslationAnnotation](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.TranslationAnnotation)`   
Annotation details for translation. This field is a member of `oneof`_ `detail`.   
`classification` |  `[google.cloud.automl_v1beta1.types.ClassificationAnnotation](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ClassificationAnnotation)`   
Annotation details for content or image classification. This field is a member of `oneof`_ `detail`.   
`image_object_detection` |  `[google.cloud.automl_v1beta1.types.ImageObjectDetectionAnnotation](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ImageObjectDetectionAnnotation)`   
Annotation details for image object detection. This field is a member of `oneof`_ `detail`.   
`video_classification` |  `[google.cloud.automl_v1beta1.types.VideoClassificationAnnotation](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.VideoClassificationAnnotation)`   
Annotation details for video classification. Returned for Video Classification predictions. This field is a member of `oneof`_ `detail`.   
`video_object_tracking` |  `[google.cloud.automl_v1beta1.types.VideoObjectTrackingAnnotation](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.VideoObjectTrackingAnnotation)`   
Annotation details for video object tracking. This field is a member of `oneof`_ `detail`.   
`text_extraction` |  `[google.cloud.automl_v1beta1.types.TextExtractionAnnotation](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.TextExtractionAnnotation)`   
Annotation details for text extraction. This field is a member of `oneof`_ `detail`.   
`text_sentiment` |  `[google.cloud.automl_v1beta1.types.TextSentimentAnnotation](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.TextSentimentAnnotation)`   
Annotation details for text sentiment. This field is a member of `oneof`_ `detail`.   
`tables` |  `[google.cloud.automl_v1beta1.types.TablesAnnotation](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.TablesAnnotation)`   
Annotation details for Tables. This field is a member of `oneof`_ `detail`.   
`annotation_spec_id` |  `str`   
Output only . The resource ID of the annotation spec that this annotation pertains to. The annotation spec comes from either an ancestor dataset, or the dataset that was used to train the model in use.   
`display_name` |  `str`   
Output only. The value of display_name when the model was trained. Because this field returns a value at model training time, for different models trained using the same dataset, the returned value could be different as model owner could update the `display_name` between any two model training.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
