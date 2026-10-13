---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-BatchPredictResult/
title: Cloud AutoML V1 API - Class Google::Cloud::AutoML::V1::BatchPredictResult (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:52:35.888160+00:00
---

# Cloud AutoML V1 API - Class Google::Cloud::AutoML::V1::BatchPredictResult (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-BatchPredictResult/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud AutoML V1 API - Class Google::Cloud::AutoML::V1::BatchPredictResult (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.0.0 (latest)  1.8.1  1.7.0  1.6.0  1.5.1  1.4.0  1.3.1  1.2.1  1.1.0  1.0.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.0  0.5.1  0.4.8 

Reference documentation and code samples for the Cloud AutoML V1 API class Google::Cloud::AutoML::V1::BatchPredictResult.

Result of the Batch Predict. This message is returned in [response](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Longrunning-Operation#Google__Longrunning__Operation_response_instance_ "Google::Longrunning::Operation#response \(method\)") of the operation returned by the [PredictionService.BatchPredict](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-PredictionService-Client#Google__Cloud__AutoML__V1__PredictionService__Client_batch_predict_instance_ "Google::Cloud::AutoML::V1::PredictionService::Client#batch_predict \(method\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #metadata
    
    
    def metadata() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Additional domain-specific prediction response metadata.

AutoML Vision Object Detection

`max_bounding_box_count` : (int64) The maximum number of bounding boxes returned per image.

AutoML Video Intelligence Object Tracking

`max_bounding_box_count` : (int64) The maximum number of bounding boxes returned per frame. 




### #metadata=
    
    
    def metadata=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Additional domain-specific prediction response metadata.

AutoML Vision Object Detection

`max_bounding_box_count` : (int64) The maximum number of bounding boxes returned per image.

AutoML Video Intelligence Object Tracking

`max_bounding_box_count` : (int64) The maximum number of bounding boxes returned per frame. 




**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Additional domain-specific prediction response metadata.

AutoML Vision Object Detection

`max_bounding_box_count` : (int64) The maximum number of bounding boxes returned per image.

AutoML Video Intelligence Object Tracking

`max_bounding_box_count` : (int64) The maximum number of bounding boxes returned per frame. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
