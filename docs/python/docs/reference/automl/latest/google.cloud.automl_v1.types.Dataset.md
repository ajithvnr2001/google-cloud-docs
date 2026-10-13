---
url: https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.Dataset
title: Class Dataset (2.21.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:57:24.771223+00:00
---

# Class Dataset (2.21.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.Dataset

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Dataset (2.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.21.0 (latest)  2.20.1  2.19.0  2.18.1  2.17.0  2.16.4  2.15.0  2.14.1  2.13.5  2.12.0  2.11.4  2.10.1  2.9.0  2.8.3  2.7.3  2.6.0  2.5.2  2.4.2  2.3.0  2.2.0  2.1.0  2.0.0  1.0.3  0.10.0  0.9.0  0.8.0  0.7.1  0.6.0  0.5.0  0.4.0 
    
    
    Dataset(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A workspace for solving a single, particular machine learning (ML) problem. A workspace contains examples that may be annotated.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`translation_dataset_metadata` |  `[google.cloud.automl_v1.types.TranslationDatasetMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.TranslationDatasetMetadata)`   
Metadata for a dataset used for translation. This field is a member of `oneof`_ `dataset_metadata`.   
`image_classification_dataset_metadata` |  `[google.cloud.automl_v1.types.ImageClassificationDatasetMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ImageClassificationDatasetMetadata)`   
Metadata for a dataset used for image classification. This field is a member of `oneof`_ `dataset_metadata`.   
`text_classification_dataset_metadata` |  `[google.cloud.automl_v1.types.TextClassificationDatasetMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.TextClassificationDatasetMetadata)`   
Metadata for a dataset used for text classification. This field is a member of `oneof`_ `dataset_metadata`.   
`image_object_detection_dataset_metadata` |  `[google.cloud.automl_v1.types.ImageObjectDetectionDatasetMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ImageObjectDetectionDatasetMetadata)`   
Metadata for a dataset used for image object detection. This field is a member of `oneof`_ `dataset_metadata`.   
`text_extraction_dataset_metadata` |  `[google.cloud.automl_v1.types.TextExtractionDatasetMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.TextExtractionDatasetMetadata)`   
Metadata for a dataset used for text extraction. This field is a member of `oneof`_ `dataset_metadata`.   
`text_sentiment_dataset_metadata` |  `[google.cloud.automl_v1.types.TextSentimentDatasetMetadata](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.TextSentimentDatasetMetadata)`   
Metadata for a dataset used for text sentiment. This field is a member of `oneof`_ `dataset_metadata`.   
`name` |  `str`   
Output only. The resource name of the dataset. Form: `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}`  
`display_name` |  `str`   
Required. The name of the dataset to show in the interface. The name can be up to 32 characters long and can consist only of ASCII Latin letters A-Z and a-z, underscores (\\_), and ASCII digits 0-9.   
`description` |  `str`   
User-provided description of the dataset. The description can be up to 25000 characters long.   
`example_count` |  `int`   
Output only. The number of examples in the dataset.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Timestamp when this dataset was created.   
`etag` |  `str`   
Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens.   
`labels` |  `MutableMapping[str, str]`   
Optional. The labels with user-defined metadata to organize your dataset. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. Label values are optional. Label keys must start with a letter. See https://goo.gl/xmQnxf for more information on and examples of labels.   
  
## Classes 

### LabelsEntry
    
    
    LabelsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The abstract base class for a message.

**Parameters**  
---  
**Name** | **Description**  
`kwargs` |  `dict`   
Keys and values corresponding to the fields of the message.  
`mapping` |  `Union[dict, `.Message`]`   
A dictionary or message to be used to determine the values for this message.  
`ignore_unknown_fields` |  `Optional(bool)`   
If True, do not raise errors for unknown fields. Only applied if `mapping` is a mapping type or there are keyword parameters.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
