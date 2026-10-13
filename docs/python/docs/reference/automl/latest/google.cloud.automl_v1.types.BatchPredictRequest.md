---
url: https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.BatchPredictRequest
title: Class BatchPredictRequest (2.21.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:57:22.871684+00:00
---

# Class BatchPredictRequest (2.21.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.BatchPredictRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class BatchPredictRequest (2.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.21.0 (latest)  2.20.1  2.19.0  2.18.1  2.17.0  2.16.4  2.15.0  2.14.1  2.13.5  2.12.0  2.11.4  2.10.1  2.9.0  2.8.3  2.7.3  2.6.0  2.5.2  2.4.2  2.3.0  2.2.0  2.1.0  2.0.0  1.0.3  0.10.0  0.9.0  0.8.0  0.7.1  0.6.0  0.5.0  0.4.0 
    
    
    BatchPredictRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Request message for PredictionService.BatchPredict.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Required. Name of the model requested to serve the batch prediction.   
`input_config` |  `[google.cloud.automl_v1.types.BatchPredictInputConfig](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.BatchPredictInputConfig)`   
Required. The input configuration for batch prediction.   
`output_config` |  `[google.cloud.automl_v1.types.BatchPredictOutputConfig](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1.types.BatchPredictOutputConfig)`   
Required. The Configuration specifying where output predictions should be written.   
`params` |  `MutableMapping[str, str]`   
Additional domain-specific parameters for the predictions, any string must be up to 25000 characters long. AutoML Natural Language Classification `score_threshold` : (float) A value from 0.0 to 1.0. When the model makes predictions for a text snippet, it will only produce results that have at least this confidence score. The default is 0.5. AutoML Vision Classification `score_threshold` : (float) A value from 0.0 to 1.0. When the model makes predictions for an image, it will only produce results that have at least this confidence score. The default is 0.5. AutoML Vision Object Detection `score_threshold` : (float) When Model detects objects on the image, it will only produce bounding boxes which have at least this confidence score. Value in 0 to 1 range, default is 0.5. `max_bounding_box_count` : (int64) The maximum number of bounding boxes returned per image. The default is 100, the number of bounding boxes returned might be limited by the server. AutoML Video Intelligence Classification `score_threshold` : (float) A value from 0.0 to 1.0. When the model makes predictions for a video, it will only produce results that have at least this confidence score. The default is 0.5. `segment_classification` : (boolean) Set to true to request segment-level classification. AutoML Video Intelligence returns labels and their confidence scores for the entire segment of the video that user specified in the request configuration. The default is true. `shot_classification` : (boolean) Set to true to request shot-level classification. AutoML Video Intelligence determines the boundaries for each camera shot in the entire segment of the video that user specified in the request configuration. AutoML Video Intelligence then returns labels and their confidence scores for each detected shot, along with the start and end time of the shot. The default is false. WARNING: Model evaluation is not done for this classification type, the quality of it depends on training data, but there are no metrics provided to describe that quality. `1s_interval_classification` : (boolean) Set to true to request classification for a video at one-second intervals. AutoML Video Intelligence returns labels and their confidence scores for each second of the entire segment of the video that user specified in the request configuration. The default is false. WARNING: Model evaluation is not done for this classification type, the quality of it depends on training data, but there are no metrics provided to describe that quality. AutoML Video Intelligence Object Tracking `score_threshold` : (float) When Model detects objects on video frames, it will only produce bounding boxes which have at least this confidence score. Value in 0 to 1 range, default is 0.5. `max_bounding_box_count` : (int64) The maximum number of bounding boxes returned per image. The default is 100, the number of bounding boxes returned might be limited by the server. `min_bounding_box_size` : (float) Only bounding boxes with shortest edge at least that long as a relative value of video frame size are returned. Value in 0 to 1 range. Default is 0.   
  
## Classes 

### ParamsEntry
    
    
    ParamsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

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
