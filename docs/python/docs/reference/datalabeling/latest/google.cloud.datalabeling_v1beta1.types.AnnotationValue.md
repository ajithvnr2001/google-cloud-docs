---
url: https://docs.cloud.google.com/python/docs/reference/datalabeling/latest/google.cloud.datalabeling_v1beta1.types.AnnotationValue
title: Class AnnotationValue (1.18.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:10:37.176722+00:00
---

# Class AnnotationValue (1.18.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/datalabeling/latest/google.cloud.datalabeling_v1beta1.types.AnnotationValue

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AnnotationValue (1.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.18.0 (latest)  1.17.0  1.16.0  1.15.0  1.14.0  1.13.2  1.12.0  1.11.1  1.10.5  1.9.0  1.8.3  1.7.0  1.6.3  1.5.2  1.4.0  1.3.0  1.2.4  1.1.0  1.0.0  0.4.2  0.3.0  0.2.1 
    
    
    AnnotationValue(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Annotation value for an example.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`image_classification_annotation` |  `[google.cloud.datalabeling_v1beta1.types.ImageClassificationAnnotation](https://docs.cloud.google.com/python/docs/reference/datalabeling/latest/google.cloud.datalabeling_v1beta1.types.ImageClassificationAnnotation)`   
Annotation value for image classification case. This field is a member of `oneof`_ `value_type`.   
`image_bounding_poly_annotation` |  `[google.cloud.datalabeling_v1beta1.types.ImageBoundingPolyAnnotation](https://docs.cloud.google.com/python/docs/reference/datalabeling/latest/google.cloud.datalabeling_v1beta1.types.ImageBoundingPolyAnnotation)`   
Annotation value for image bounding box, oriented bounding box and polygon cases. This field is a member of `oneof`_ `value_type`.   
`image_polyline_annotation` |  `[google.cloud.datalabeling_v1beta1.types.ImagePolylineAnnotation](https://docs.cloud.google.com/python/docs/reference/datalabeling/latest/google.cloud.datalabeling_v1beta1.types.ImagePolylineAnnotation)`   
Annotation value for image polyline cases. Polyline here is different from BoundingPoly. It is formed by line segments connected to each other but not closed form(Bounding Poly). The line segments can cross each other. This field is a member of `oneof`_ `value_type`.   
`image_segmentation_annotation` |  `[google.cloud.datalabeling_v1beta1.types.ImageSegmentationAnnotation](https://docs.cloud.google.com/python/docs/reference/datalabeling/latest/google.cloud.datalabeling_v1beta1.types.ImageSegmentationAnnotation)`   
Annotation value for image segmentation. This field is a member of `oneof`_ `value_type`.   
`text_classification_annotation` |  `[google.cloud.datalabeling_v1beta1.types.TextClassificationAnnotation](https://docs.cloud.google.com/python/docs/reference/datalabeling/latest/google.cloud.datalabeling_v1beta1.types.TextClassificationAnnotation)`   
Annotation value for text classification case. This field is a member of `oneof`_ `value_type`.   
`text_entity_extraction_annotation` |  `[google.cloud.datalabeling_v1beta1.types.TextEntityExtractionAnnotation](https://docs.cloud.google.com/python/docs/reference/datalabeling/latest/google.cloud.datalabeling_v1beta1.types.TextEntityExtractionAnnotation)`   
Annotation value for text entity extraction case. This field is a member of `oneof`_ `value_type`.   
`video_classification_annotation` |  `[google.cloud.datalabeling_v1beta1.types.VideoClassificationAnnotation](https://docs.cloud.google.com/python/docs/reference/datalabeling/latest/google.cloud.datalabeling_v1beta1.types.VideoClassificationAnnotation)`   
Annotation value for video classification case. This field is a member of `oneof`_ `value_type`.   
`video_object_tracking_annotation` |  `[google.cloud.datalabeling_v1beta1.types.VideoObjectTrackingAnnotation](https://docs.cloud.google.com/python/docs/reference/datalabeling/latest/google.cloud.datalabeling_v1beta1.types.VideoObjectTrackingAnnotation)`   
Annotation value for video object detection and tracking case. This field is a member of `oneof`_ `value_type`.   
`video_event_annotation` |  `[google.cloud.datalabeling_v1beta1.types.VideoEventAnnotation](https://docs.cloud.google.com/python/docs/reference/datalabeling/latest/google.cloud.datalabeling_v1beta1.types.VideoEventAnnotation)`   
Annotation value for video event case. This field is a member of `oneof`_ `value_type`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
