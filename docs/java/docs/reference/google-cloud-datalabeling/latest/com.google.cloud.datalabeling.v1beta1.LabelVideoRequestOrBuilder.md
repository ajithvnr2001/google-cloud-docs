---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.LabelVideoRequestOrBuilder
title: Interface LabelVideoRequestOrBuilder (0.215.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:49:18.087903+00:00
---

# Interface LabelVideoRequestOrBuilder (0.215.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.LabelVideoRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface LabelVideoRequestOrBuilder (0.215.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.215.0 (latest)  0.214.0  0.213.0  0.211.0  0.208.0  0.207.0  0.205.0  0.203.0  0.202.0  0.201.0  0.200.0  0.198.0  0.196.0  0.195.0  0.194.0  0.193.0  0.192.0  0.190.0  0.188.0  0.187.0  0.184.0  0.183.0  0.182.0  0.180.0  0.179.0  0.178.0  0.177.0  0.176.0  0.175.0  0.174.0  0.173.0  0.172.0  0.171.0  0.169.0  0.168.0  0.167.0  0.166.0  0.165.0  0.164.0  0.163.0  0.162.0  0.161.0  0.160.0  0.159.0  0.157.0  0.156.0  0.155.0  0.154.0  0.153.0  0.152.0  0.151.0  0.150.0  0.149.0  0.148.0  0.147.0  0.144.0  0.143.0  0.142.0  0.141.0  0.140.0  0.139.0  0.138.0  0.137.0  0.136.0  0.135.0  0.134.0  0.133.0  0.132.0  0.131.0  0.129.0  0.128.0  0.127.0  0.126.0  0.125.0  0.124.0  0.123.7  0.122.11 
    
    
    public interface LabelVideoRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getBasicConfig()
    
    
    public abstract HumanAnnotationConfig getBasicConfig()

Required. Basic human annotation config.

` .google.cloud.datalabeling.v1beta1.HumanAnnotationConfig basic_config = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[HumanAnnotationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.HumanAnnotationConfig)` | The basicConfig.  
  
### getBasicConfigOrBuilder()
    
    
    public abstract HumanAnnotationConfigOrBuilder getBasicConfigOrBuilder()

Required. Basic human annotation config.

` .google.cloud.datalabeling.v1beta1.HumanAnnotationConfig basic_config = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[HumanAnnotationConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.HumanAnnotationConfigOrBuilder)` |   
  
### getEventConfig()
    
    
    public abstract EventConfig getEventConfig()

Configuration for video event task. One of video_classification_config, object_detection_config, object_tracking_config and event_config is required.

`.google.cloud.datalabeling.v1beta1.EventConfig event_config = 7;`

**Returns**  
---  
**Type** | **Description**  
`[EventConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.EventConfig)` | The eventConfig.  
  
### getEventConfigOrBuilder()
    
    
    public abstract EventConfigOrBuilder getEventConfigOrBuilder()

Configuration for video event task. One of video_classification_config, object_detection_config, object_tracking_config and event_config is required.

`.google.cloud.datalabeling.v1beta1.EventConfig event_config = 7;`

**Returns**  
---  
**Type** | **Description**  
`[EventConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.EventConfigOrBuilder)` |   
  
### getFeature()
    
    
    public abstract LabelVideoRequest.Feature getFeature()

Required. The type of video labeling task.

` .google.cloud.datalabeling.v1beta1.LabelVideoRequest.Feature feature = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[LabelVideoRequest.Feature](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.LabelVideoRequest.Feature)` | The feature.  
  
### getFeatureValue()
    
    
    public abstract int getFeatureValue()

Required. The type of video labeling task.

` .google.cloud.datalabeling.v1beta1.LabelVideoRequest.Feature feature = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for feature.  
  
### getObjectDetectionConfig()
    
    
    public abstract ObjectDetectionConfig getObjectDetectionConfig()

Configuration for video object detection task. One of video_classification_config, object_detection_config, object_tracking_config and event_config is required.

`.google.cloud.datalabeling.v1beta1.ObjectDetectionConfig object_detection_config = 5; `

**Returns**  
---  
**Type** | **Description**  
`[ObjectDetectionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.ObjectDetectionConfig)` | The objectDetectionConfig.  
  
### getObjectDetectionConfigOrBuilder()
    
    
    public abstract ObjectDetectionConfigOrBuilder getObjectDetectionConfigOrBuilder()

Configuration for video object detection task. One of video_classification_config, object_detection_config, object_tracking_config and event_config is required.

`.google.cloud.datalabeling.v1beta1.ObjectDetectionConfig object_detection_config = 5; `

**Returns**  
---  
**Type** | **Description**  
`[ObjectDetectionConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.ObjectDetectionConfigOrBuilder)` |   
  
### getObjectTrackingConfig()
    
    
    public abstract ObjectTrackingConfig getObjectTrackingConfig()

Configuration for video object tracking task. One of video_classification_config, object_detection_config, object_tracking_config and event_config is required.

`.google.cloud.datalabeling.v1beta1.ObjectTrackingConfig object_tracking_config = 6; `

**Returns**  
---  
**Type** | **Description**  
`[ObjectTrackingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.ObjectTrackingConfig)` | The objectTrackingConfig.  
  
### getObjectTrackingConfigOrBuilder()
    
    
    public abstract ObjectTrackingConfigOrBuilder getObjectTrackingConfigOrBuilder()

Configuration for video object tracking task. One of video_classification_config, object_detection_config, object_tracking_config and event_config is required.

`.google.cloud.datalabeling.v1beta1.ObjectTrackingConfig object_tracking_config = 6; `

**Returns**  
---  
**Type** | **Description**  
`[ObjectTrackingConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.ObjectTrackingConfigOrBuilder)` |   
  
### getParent()
    
    
    public abstract String getParent()

Required. Name of the dataset to request labeling task, format: projects/{project_id}/datasets/{dataset_id}

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The parent.  
  
### getParentBytes()
    
    
    public abstract ByteString getParentBytes()

Required. Name of the dataset to request labeling task, format: projects/{project_id}/datasets/{dataset_id}

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for parent.  
  
### getRequestConfigCase()
    
    
    public abstract LabelVideoRequest.RequestConfigCase getRequestConfigCase()

**Returns**  
---  
**Type** | **Description**  
`[LabelVideoRequest.RequestConfigCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.LabelVideoRequest.RequestConfigCase)` |   
  
### getVideoClassificationConfig()
    
    
    public abstract VideoClassificationConfig getVideoClassificationConfig()

Configuration for video classification task. One of video_classification_config, object_detection_config, object_tracking_config and event_config is required.

` .google.cloud.datalabeling.v1beta1.VideoClassificationConfig video_classification_config = 4; `

**Returns**  
---  
**Type** | **Description**  
`[VideoClassificationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.VideoClassificationConfig)` | The videoClassificationConfig.  
  
### getVideoClassificationConfigOrBuilder()
    
    
    public abstract VideoClassificationConfigOrBuilder getVideoClassificationConfigOrBuilder()

Configuration for video classification task. One of video_classification_config, object_detection_config, object_tracking_config and event_config is required.

` .google.cloud.datalabeling.v1beta1.VideoClassificationConfig video_classification_config = 4; `

**Returns**  
---  
**Type** | **Description**  
`[VideoClassificationConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.VideoClassificationConfigOrBuilder)` |   
  
### hasBasicConfig()
    
    
    public abstract boolean hasBasicConfig()

Required. Basic human annotation config.

` .google.cloud.datalabeling.v1beta1.HumanAnnotationConfig basic_config = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the basicConfig field is set.  
  
### hasEventConfig()
    
    
    public abstract boolean hasEventConfig()

Configuration for video event task. One of video_classification_config, object_detection_config, object_tracking_config and event_config is required.

`.google.cloud.datalabeling.v1beta1.EventConfig event_config = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the eventConfig field is set.  
  
### hasObjectDetectionConfig()
    
    
    public abstract boolean hasObjectDetectionConfig()

Configuration for video object detection task. One of video_classification_config, object_detection_config, object_tracking_config and event_config is required.

`.google.cloud.datalabeling.v1beta1.ObjectDetectionConfig object_detection_config = 5; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the objectDetectionConfig field is set.  
  
### hasObjectTrackingConfig()
    
    
    public abstract boolean hasObjectTrackingConfig()

Configuration for video object tracking task. One of video_classification_config, object_detection_config, object_tracking_config and event_config is required.

`.google.cloud.datalabeling.v1beta1.ObjectTrackingConfig object_tracking_config = 6; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the objectTrackingConfig field is set.  
  
### hasVideoClassificationConfig()
    
    
    public abstract boolean hasVideoClassificationConfig()

Configuration for video classification task. One of video_classification_config, object_detection_config, object_tracking_config and event_config is required.

` .google.cloud.datalabeling.v1beta1.VideoClassificationConfig video_classification_config = 4; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the videoClassificationConfig field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
