---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-PredictRequest/
title: Cloud AutoML V1 API - Class Google::Cloud::AutoML::V1::PredictRequest (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:34:08.199777+00:00
---

# Cloud AutoML V1 API - Class Google::Cloud::AutoML::V1::PredictRequest (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-PredictRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud AutoML V1 API - Class Google::Cloud::AutoML::V1::PredictRequest (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.0.0 (latest)  1.8.1  1.7.0  1.6.0  1.5.1  1.4.0  1.3.1  1.2.1  1.1.0  1.0.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.0  0.5.1  0.4.8 

Reference documentation and code samples for the Cloud AutoML V1 API class Google::Cloud::AutoML::V1::PredictRequest.

Request message for [PredictionService.Predict](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-PredictionService-Client#Google__Cloud__AutoML__V1__PredictionService__Client_predict_instance_ "Google::Cloud::AutoML::V1::PredictionService::Client#predict \(method\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Required. Name of the model requested to serve the prediction. 



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Name of the model requested to serve the prediction. 



**Returns**

  * (::String) — Required. Name of the model requested to serve the prediction. 



### #params
    
    
    def params() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Additional domain-specific parameters, any string must be up to 25000 characters long.

AutoML Vision Classification

`score_threshold` : (float) A value from 0.0 to 1.0. When the model makes predictions for an image, it will only produce results that have at least this confidence score. The default is 0.5.

AutoML Vision Object Detection

`score_threshold` : (float) When Model detects objects on the image, it will only produce bounding boxes which have at least this confidence score. Value in 0 to 1 range, default is 0.5.

`max_bounding_box_count` : (int64) The maximum number of bounding boxes returned. The default is 100. The number of returned bounding boxes might be limited by the server.

AutoML Tables

`feature_importance` : (boolean) Whether [feature_importance][google.cloud.automl.v1.TablesModelColumnInfo.feature_importance] is populated in the returned list of [TablesAnnotation][google.cloud.automl.v1.TablesAnnotation] objects. The default is false. 




### #params=
    
    
    def params=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Additional domain-specific parameters, any string must be up to 25000 characters long.

AutoML Vision Classification

`score_threshold` : (float) A value from 0.0 to 1.0. When the model makes predictions for an image, it will only produce results that have at least this confidence score. The default is 0.5.

AutoML Vision Object Detection

`score_threshold` : (float) When Model detects objects on the image, it will only produce bounding boxes which have at least this confidence score. Value in 0 to 1 range, default is 0.5.

`max_bounding_box_count` : (int64) The maximum number of bounding boxes returned. The default is 100. The number of returned bounding boxes might be limited by the server.

AutoML Tables

`feature_importance` : (boolean) Whether [feature_importance][google.cloud.automl.v1.TablesModelColumnInfo.feature_importance] is populated in the returned list of [TablesAnnotation][google.cloud.automl.v1.TablesAnnotation] objects. The default is false. 




**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Additional domain-specific parameters, any string must be up to 25000 characters long.

AutoML Vision Classification

`score_threshold` : (float) A value from 0.0 to 1.0. When the model makes predictions for an image, it will only produce results that have at least this confidence score. The default is 0.5.

AutoML Vision Object Detection

`score_threshold` : (float) When Model detects objects on the image, it will only produce bounding boxes which have at least this confidence score. Value in 0 to 1 range, default is 0.5.

`max_bounding_box_count` : (int64) The maximum number of bounding boxes returned. The default is 100. The number of returned bounding boxes might be limited by the server.

AutoML Tables

`feature_importance` : (boolean) Whether [feature_importance][google.cloud.automl.v1.TablesModelColumnInfo.feature_importance] is populated in the returned list of [TablesAnnotation][google.cloud.automl.v1.TablesAnnotation] objects. The default is false. 




### #payload
    
    
    def payload() -> ::Google::Cloud::AutoML::V1::ExamplePayload

**Returns**

  * ([::Google::Cloud::AutoML::V1::ExamplePayload](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-ExamplePayload)) — Required. Payload to perform a prediction on. The payload must match the problem type that the model was trained to solve. 



### #payload=
    
    
    def payload=(value) -> ::Google::Cloud::AutoML::V1::ExamplePayload

**Parameter**

  * **value** ([::Google::Cloud::AutoML::V1::ExamplePayload](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-ExamplePayload)) — Required. Payload to perform a prediction on. The payload must match the problem type that the model was trained to solve. 



**Returns**

  * ([::Google::Cloud::AutoML::V1::ExamplePayload](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-automl-v1/latest/Google-Cloud-AutoML-V1-ExamplePayload)) — Required. Payload to perform a prediction on. The payload must match the problem type that the model was trained to solve. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
