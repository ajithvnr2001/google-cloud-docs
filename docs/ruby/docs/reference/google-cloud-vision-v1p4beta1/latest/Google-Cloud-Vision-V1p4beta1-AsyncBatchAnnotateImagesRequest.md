---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p4beta1/latest/Google-Cloud-Vision-V1p4beta1-AsyncBatchAnnotateImagesRequest/
title: Cloud Vision V1p4beta1 API - Class Google::Cloud::Vision::V1p4beta1::AsyncBatchAnnotateImagesRequest (v0.16.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:00:09.481472+00:00
---

# Cloud Vision V1p4beta1 API - Class Google::Cloud::Vision::V1p4beta1::AsyncBatchAnnotateImagesRequest (v0.16.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p4beta1/latest/Google-Cloud-Vision-V1p4beta1-AsyncBatchAnnotateImagesRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Vision V1p4beta1 API - Class Google::Cloud::Vision::V1p4beta1::AsyncBatchAnnotateImagesRequest (v0.16.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.16.1 (latest)  0.16.0  0.15.1  0.14.1  0.13.0  0.12.1  0.11.1  0.10.0  0.9.0  0.8.1  0.7.2  0.6.0  0.5.1  0.4.0  0.3.0  0.2.0  0.1.2 

Reference documentation and code samples for the Cloud Vision V1p4beta1 API class Google::Cloud::Vision::V1p4beta1::AsyncBatchAnnotateImagesRequest.

Request for async image annotation for a list of images.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #output_config
    
    
    def output_config() -> ::Google::Cloud::Vision::V1p4beta1::OutputConfig

**Returns**

  * ([::Google::Cloud::Vision::V1p4beta1::OutputConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p4beta1/latest/Google-Cloud-Vision-V1p4beta1-OutputConfig)) — Required. The desired output location and metadata (e.g. format). 



### #output_config=
    
    
    def output_config=(value) -> ::Google::Cloud::Vision::V1p4beta1::OutputConfig

**Parameter**

  * **value** ([::Google::Cloud::Vision::V1p4beta1::OutputConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p4beta1/latest/Google-Cloud-Vision-V1p4beta1-OutputConfig)) — Required. The desired output location and metadata (e.g. format). 



**Returns**

  * ([::Google::Cloud::Vision::V1p4beta1::OutputConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p4beta1/latest/Google-Cloud-Vision-V1p4beta1-OutputConfig)) — Required. The desired output location and metadata (e.g. format). 



### #requests
    
    
    def requests() -> ::Array<::Google::Cloud::Vision::V1p4beta1::AnnotateImageRequest>

**Returns**

  * (::Array<[::Google::Cloud::Vision::V1p4beta1::AnnotateImageRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p4beta1/latest/Google-Cloud-Vision-V1p4beta1-AnnotateImageRequest)>) — Required. Individual image annotation requests for this batch. 



### #requests=
    
    
    def requests=(value) -> ::Array<::Google::Cloud::Vision::V1p4beta1::AnnotateImageRequest>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Vision::V1p4beta1::AnnotateImageRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p4beta1/latest/Google-Cloud-Vision-V1p4beta1-AnnotateImageRequest)>) — Required. Individual image annotation requests for this batch. 



**Returns**

  * (::Array<[::Google::Cloud::Vision::V1p4beta1::AnnotateImageRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p4beta1/latest/Google-Cloud-Vision-V1p4beta1-AnnotateImageRequest)>) — Required. Individual image annotation requests for this batch. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
