---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Cloud-DataLabeling-V1beta1-LabelVideoRequest/
title: AI Platform Data Labeling Service V1beta1 API - Class Google::Cloud::DataLabeling::V1beta1::LabelVideoRequest (v0.16.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:01:09.641849+00:00
---

# AI Platform Data Labeling Service V1beta1 API - Class Google::Cloud::DataLabeling::V1beta1::LabelVideoRequest (v0.16.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Cloud-DataLabeling-V1beta1-LabelVideoRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  AI Platform Data Labeling Service V1beta1 API - Class Google::Cloud::DataLabeling::V1beta1::LabelVideoRequest (v0.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.16.0 (latest)  0.15.0  0.14.0  0.13.1  0.12.0  0.11.1  0.10.1  0.9.0  0.8.1  0.7.2  0.6.0  0.5.0  0.4.0  0.3.5 

Reference documentation and code samples for the AI Platform Data Labeling Service V1beta1 API class Google::Cloud::DataLabeling::V1beta1::LabelVideoRequest.

Request message for LabelVideo.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #basic_config
    
    
    def basic_config() -> ::Google::Cloud::DataLabeling::V1beta1::HumanAnnotationConfig

**Returns**

  * ([::Google::Cloud::DataLabeling::V1beta1::HumanAnnotationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Cloud-DataLabeling-V1beta1-HumanAnnotationConfig)) — Required. Basic human annotation config. 



### #basic_config=
    
    
    def basic_config=(value) -> ::Google::Cloud::DataLabeling::V1beta1::HumanAnnotationConfig

**Parameter**

  * **value** ([::Google::Cloud::DataLabeling::V1beta1::HumanAnnotationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Cloud-DataLabeling-V1beta1-HumanAnnotationConfig)) — Required. Basic human annotation config. 



**Returns**

  * ([::Google::Cloud::DataLabeling::V1beta1::HumanAnnotationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Cloud-DataLabeling-V1beta1-HumanAnnotationConfig)) — Required. Basic human annotation config. 



### #event_config
    
    
    def event_config() -> ::Google::Cloud::DataLabeling::V1beta1::EventConfig

**Returns**

  * ([::Google::Cloud::DataLabeling::V1beta1::EventConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Cloud-DataLabeling-V1beta1-EventConfig)) — Configuration for video event task. One of video_classification_config, object_detection_config, object_tracking_config and event_config is required.

Note: The following fields are mutually exclusive: `event_config`, `video_classification_config`, `object_detection_config`, `object_tracking_config`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #event_config=
    
    
    def event_config=(value) -> ::Google::Cloud::DataLabeling::V1beta1::EventConfig

**Parameter**

  * **value** ([::Google::Cloud::DataLabeling::V1beta1::EventConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Cloud-DataLabeling-V1beta1-EventConfig)) — Configuration for video event task. One of video_classification_config, object_detection_config, object_tracking_config and event_config is required.

Note: The following fields are mutually exclusive: `event_config`, `video_classification_config`, `object_detection_config`, `object_tracking_config`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::DataLabeling::V1beta1::EventConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Cloud-DataLabeling-V1beta1-EventConfig)) — Configuration for video event task. One of video_classification_config, object_detection_config, object_tracking_config and event_config is required.

Note: The following fields are mutually exclusive: `event_config`, `video_classification_config`, `object_detection_config`, `object_tracking_config`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #feature
    
    
    def feature() -> ::Google::Cloud::DataLabeling::V1beta1::LabelVideoRequest::Feature

**Returns**

  * ([::Google::Cloud::DataLabeling::V1beta1::LabelVideoRequest::Feature](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Cloud-DataLabeling-V1beta1-LabelVideoRequest-Feature)) — Required. The type of video labeling task. 



### #feature=
    
    
    def feature=(value) -> ::Google::Cloud::DataLabeling::V1beta1::LabelVideoRequest::Feature

**Parameter**

  * **value** ([::Google::Cloud::DataLabeling::V1beta1::LabelVideoRequest::Feature](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Cloud-DataLabeling-V1beta1-LabelVideoRequest-Feature)) — Required. The type of video labeling task. 



**Returns**

  * ([::Google::Cloud::DataLabeling::V1beta1::LabelVideoRequest::Feature](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Cloud-DataLabeling-V1beta1-LabelVideoRequest-Feature)) — Required. The type of video labeling task. 



### #object_detection_config
    
    
    def object_detection_config() -> ::Google::Cloud::DataLabeling::V1beta1::ObjectDetectionConfig

**Returns**

  * ([::Google::Cloud::DataLabeling::V1beta1::ObjectDetectionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Cloud-DataLabeling-V1beta1-ObjectDetectionConfig)) — Configuration for video object detection task. One of video_classification_config, object_detection_config, object_tracking_config and event_config is required.

Note: The following fields are mutually exclusive: `object_detection_config`, `video_classification_config`, `object_tracking_config`, `event_config`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #object_detection_config=
    
    
    def object_detection_config=(value) -> ::Google::Cloud::DataLabeling::V1beta1::ObjectDetectionConfig

**Parameter**

  * **value** ([::Google::Cloud::DataLabeling::V1beta1::ObjectDetectionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Cloud-DataLabeling-V1beta1-ObjectDetectionConfig)) — Configuration for video object detection task. One of video_classification_config, object_detection_config, object_tracking_config and event_config is required.

Note: The following fields are mutually exclusive: `object_detection_config`, `video_classification_config`, `object_tracking_config`, `event_config`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::DataLabeling::V1beta1::ObjectDetectionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Cloud-DataLabeling-V1beta1-ObjectDetectionConfig)) — Configuration for video object detection task. One of video_classification_config, object_detection_config, object_tracking_config and event_config is required.

Note: The following fields are mutually exclusive: `object_detection_config`, `video_classification_config`, `object_tracking_config`, `event_config`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #object_tracking_config
    
    
    def object_tracking_config() -> ::Google::Cloud::DataLabeling::V1beta1::ObjectTrackingConfig

**Returns**

  * ([::Google::Cloud::DataLabeling::V1beta1::ObjectTrackingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Cloud-DataLabeling-V1beta1-ObjectTrackingConfig)) — Configuration for video object tracking task. One of video_classification_config, object_detection_config, object_tracking_config and event_config is required.

Note: The following fields are mutually exclusive: `object_tracking_config`, `video_classification_config`, `object_detection_config`, `event_config`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #object_tracking_config=
    
    
    def object_tracking_config=(value) -> ::Google::Cloud::DataLabeling::V1beta1::ObjectTrackingConfig

**Parameter**

  * **value** ([::Google::Cloud::DataLabeling::V1beta1::ObjectTrackingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Cloud-DataLabeling-V1beta1-ObjectTrackingConfig)) — Configuration for video object tracking task. One of video_classification_config, object_detection_config, object_tracking_config and event_config is required.

Note: The following fields are mutually exclusive: `object_tracking_config`, `video_classification_config`, `object_detection_config`, `event_config`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::DataLabeling::V1beta1::ObjectTrackingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Cloud-DataLabeling-V1beta1-ObjectTrackingConfig)) — Configuration for video object tracking task. One of video_classification_config, object_detection_config, object_tracking_config and event_config is required.

Note: The following fields are mutually exclusive: `object_tracking_config`, `video_classification_config`, `object_detection_config`, `event_config`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. Name of the dataset to request labeling task, format: projects/{project_id}/datasets/{dataset_id} 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Name of the dataset to request labeling task, format: projects/{project_id}/datasets/{dataset_id} 



**Returns**

  * (::String) — Required. Name of the dataset to request labeling task, format: projects/{project_id}/datasets/{dataset_id} 



### #video_classification_config
    
    
    def video_classification_config() -> ::Google::Cloud::DataLabeling::V1beta1::VideoClassificationConfig

**Returns**

  * ([::Google::Cloud::DataLabeling::V1beta1::VideoClassificationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Cloud-DataLabeling-V1beta1-VideoClassificationConfig)) — Configuration for video classification task. One of video_classification_config, object_detection_config, object_tracking_config and event_config is required.

Note: The following fields are mutually exclusive: `video_classification_config`, `object_detection_config`, `object_tracking_config`, `event_config`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #video_classification_config=
    
    
    def video_classification_config=(value) -> ::Google::Cloud::DataLabeling::V1beta1::VideoClassificationConfig

**Parameter**

  * **value** ([::Google::Cloud::DataLabeling::V1beta1::VideoClassificationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Cloud-DataLabeling-V1beta1-VideoClassificationConfig)) — Configuration for video classification task. One of video_classification_config, object_detection_config, object_tracking_config and event_config is required.

Note: The following fields are mutually exclusive: `video_classification_config`, `object_detection_config`, `object_tracking_config`, `event_config`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::DataLabeling::V1beta1::VideoClassificationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-data_labeling-v1beta1/latest/Google-Cloud-DataLabeling-V1beta1-VideoClassificationConfig)) — Configuration for video classification task. One of video_classification_config, object_detection_config, object_tracking_config and event_config is required.

Note: The following fields are mutually exclusive: `video_classification_config`, `object_detection_config`, `object_tracking_config`, `event_config`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
