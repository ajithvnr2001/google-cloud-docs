---
url: https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.PredictResponse
title: Class PredictResponse (2.21.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:57:32.425880+00:00
---

# Class PredictResponse (2.21.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.PredictResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class PredictResponse (2.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.21.0 (latest)  2.20.1  2.19.0  2.18.1  2.17.0  2.16.4  2.15.0  2.14.1  2.13.5  2.12.0  2.11.4  2.10.1  2.9.0  2.8.3  2.7.3  2.6.0  2.5.2  2.4.2  2.3.0  2.2.0  2.1.0  2.0.0  1.0.3  0.10.0  0.9.0  0.8.0  0.7.1  0.6.0  0.5.0  0.4.0 
    
    
    PredictResponse(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Response message for PredictionService.Predict.

## Attributes  
  
---  
**Name** | **Description**  
`payload` |  `MutableSequence[[google.cloud.automl_v1.types.AnnotationPayload](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.AnnotationPayload)]`   
Prediction result. AutoML Translation and AutoML Natural Language Sentiment Analysis return precisely one payload.   
`preprocessed_input` |  `[google.cloud.automl_v1.types.ExamplePayload](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.ExamplePayload)`   
The preprocessed example that AutoML actually makes prediction on. Empty if AutoML does not preprocess the input example. For AutoML Natural Language (Classification, Entity Extraction, and Sentiment Analysis), if the input is a document, the recognized text is returned in the document_text property.   
`metadata` |  `MutableMapping[str, str]`   
Additional domain-specific prediction response metadata. AutoML Vision Object Detection `max_bounding_box_count` : (int64) The maximum number of bounding boxes to return per image. AutoML Natural Language Sentiment Analysis `sentiment_score` : (float, deprecated) A value between -1 and 1, -1 maps to least positive sentiment, while 1 maps to the most positive one and the higher the score, the more positive the sentiment in the document is. Yet these values are relative to the training data, so e.g. if all data was positive then -1 is also positive (though the least). `sentiment_score` is not the same as "score" and "magnitude" from Sentiment Analysis in the Natural Language API.   
  
## Classes 

### MetadataEntry
    
    
    MetadataEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

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
