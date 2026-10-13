---
url: https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ModelEvaluation
title: Class ModelEvaluation (2.21.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:57:31.617596+00:00
---

# Class ModelEvaluation (2.21.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ModelEvaluation

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ModelEvaluation (2.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.21.0 (latest)  2.20.1  2.19.0  2.18.1  2.17.0  2.16.4  2.15.0  2.14.1  2.13.5  2.12.0  2.11.4  2.10.1  2.9.0  2.8.3  2.7.3  2.6.0  2.5.2  2.4.2  2.3.0  2.2.0  2.1.0  2.0.0  1.0.3  0.10.0  0.9.0  0.8.0  0.7.1  0.6.0  0.5.0  0.4.0 
    
    
    ModelEvaluation(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Evaluation results of a model.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`classification_evaluation_metrics` |  `[google.cloud.automl_v1.types.ClassificationEvaluationMetrics](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ClassificationEvaluationMetrics)`   
Model evaluation metrics for image, text, video and tables classification. Tables problem is considered a classification when the target column is CATEGORY DataType. This field is a member of `oneof`_ `metrics`.   
`translation_evaluation_metrics` |  `[google.cloud.automl_v1.types.TranslationEvaluationMetrics](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.TranslationEvaluationMetrics)`   
Model evaluation metrics for translation. This field is a member of `oneof`_ `metrics`.   
`image_object_detection_evaluation_metrics` |  `[google.cloud.automl_v1.types.ImageObjectDetectionEvaluationMetrics](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ImageObjectDetectionEvaluationMetrics)`   
Model evaluation metrics for image object detection. This field is a member of `oneof`_ `metrics`.   
`text_sentiment_evaluation_metrics` |  `[google.cloud.automl_v1.types.TextSentimentEvaluationMetrics](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.TextSentimentEvaluationMetrics)`   
Evaluation metrics for text sentiment models. This field is a member of `oneof`_ `metrics`.   
`text_extraction_evaluation_metrics` |  `[google.cloud.automl_v1.types.TextExtractionEvaluationMetrics](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.TextExtractionEvaluationMetrics)`   
Evaluation metrics for text extraction models. This field is a member of `oneof`_ `metrics`.   
`name` |  `str`   
Output only. Resource name of the model evaluation. Format: `projects/{project_id}/locations/{location_id}/models/{model_id}/modelEvaluations/{model_evaluation_id}`  
`annotation_spec_id` |  `str`   
Output only. The ID of the annotation spec that the model evaluation applies to. The The ID is empty for the overall model evaluation. For Tables annotation specs in the dataset do not exist and this ID is always not set, but for CLASSIFICATION prediction_type-s the display_name field is used.   
`display_name` |  `str`   
Output only. The value of display_name at the moment when the model was trained. Because this field returns a value at model training time, for different models trained from the same dataset, the values may differ, since display names could had been changed between the two model's trainings. For Tables CLASSIFICATION prediction_type-s distinct values of the target column at the moment of the model evaluation are populated here. The display_name is empty for the overall model evaluation.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Timestamp when this model evaluation was created.   
`evaluated_example_count` |  `int`   
Output only. The number of examples used for model evaluation, i.e. for which ground truth from time of model creation is compared against the predicted annotations created by the model. For overall ModelEvaluation (i.e. with annotation_spec_id not set) this is the total number of all examples used for evaluation. Otherwise, this is the count of examples that according to the ground truth were annotated by the annotation_spec_id.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
