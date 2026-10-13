---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p3beta1/latest/Google-Cloud-Vision-V1p3beta1-AsyncAnnotateFileRequest/
title: Cloud Vision V1p3beta1 API - Class Google::Cloud::Vision::V1p3beta1::AsyncAnnotateFileRequest (v0.20.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:51:26.541298+00:00
---

# Cloud Vision V1p3beta1 API - Class Google::Cloud::Vision::V1p3beta1::AsyncAnnotateFileRequest (v0.20.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p3beta1/latest/Google-Cloud-Vision-V1p3beta1-AsyncAnnotateFileRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Vision V1p3beta1 API - Class Google::Cloud::Vision::V1p3beta1::AsyncAnnotateFileRequest (v0.20.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.1 (latest)  0.20.0  0.19.1  0.18.1  0.17.0  0.16.0  0.15.1  0.14.0  0.13.1  0.12.2  0.11.0  0.10.1  0.9.0  0.8.0  0.7.0  0.6.0  0.5.5 

Reference documentation and code samples for the Cloud Vision V1p3beta1 API class Google::Cloud::Vision::V1p3beta1::AsyncAnnotateFileRequest.

An offline file annotation request.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #features
    
    
    def features() -> ::Array<::Google::Cloud::Vision::V1p3beta1::Feature>

**Returns**

  * (::Array<[::Google::Cloud::Vision::V1p3beta1::Feature](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p3beta1/latest/Google-Cloud-Vision-V1p3beta1-Feature)>) — Required. Requested features. 



### #features=
    
    
    def features=(value) -> ::Array<::Google::Cloud::Vision::V1p3beta1::Feature>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Vision::V1p3beta1::Feature](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p3beta1/latest/Google-Cloud-Vision-V1p3beta1-Feature)>) — Required. Requested features. 



**Returns**

  * (::Array<[::Google::Cloud::Vision::V1p3beta1::Feature](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p3beta1/latest/Google-Cloud-Vision-V1p3beta1-Feature)>) — Required. Requested features. 



### #image_context
    
    
    def image_context() -> ::Google::Cloud::Vision::V1p3beta1::ImageContext

**Returns**

  * ([::Google::Cloud::Vision::V1p3beta1::ImageContext](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p3beta1/latest/Google-Cloud-Vision-V1p3beta1-ImageContext)) — Additional context that may accompany the image(s) in the file. 



### #image_context=
    
    
    def image_context=(value) -> ::Google::Cloud::Vision::V1p3beta1::ImageContext

**Parameter**

  * **value** ([::Google::Cloud::Vision::V1p3beta1::ImageContext](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p3beta1/latest/Google-Cloud-Vision-V1p3beta1-ImageContext)) — Additional context that may accompany the image(s) in the file. 



**Returns**

  * ([::Google::Cloud::Vision::V1p3beta1::ImageContext](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p3beta1/latest/Google-Cloud-Vision-V1p3beta1-ImageContext)) — Additional context that may accompany the image(s) in the file. 



### #input_config
    
    
    def input_config() -> ::Google::Cloud::Vision::V1p3beta1::InputConfig

**Returns**

  * ([::Google::Cloud::Vision::V1p3beta1::InputConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p3beta1/latest/Google-Cloud-Vision-V1p3beta1-InputConfig)) — Required. Information about the input file. 



### #input_config=
    
    
    def input_config=(value) -> ::Google::Cloud::Vision::V1p3beta1::InputConfig

**Parameter**

  * **value** ([::Google::Cloud::Vision::V1p3beta1::InputConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p3beta1/latest/Google-Cloud-Vision-V1p3beta1-InputConfig)) — Required. Information about the input file. 



**Returns**

  * ([::Google::Cloud::Vision::V1p3beta1::InputConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p3beta1/latest/Google-Cloud-Vision-V1p3beta1-InputConfig)) — Required. Information about the input file. 



### #output_config
    
    
    def output_config() -> ::Google::Cloud::Vision::V1p3beta1::OutputConfig

**Returns**

  * ([::Google::Cloud::Vision::V1p3beta1::OutputConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p3beta1/latest/Google-Cloud-Vision-V1p3beta1-OutputConfig)) — Required. The desired output location and metadata (e.g. format). 



### #output_config=
    
    
    def output_config=(value) -> ::Google::Cloud::Vision::V1p3beta1::OutputConfig

**Parameter**

  * **value** ([::Google::Cloud::Vision::V1p3beta1::OutputConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p3beta1/latest/Google-Cloud-Vision-V1p3beta1-OutputConfig)) — Required. The desired output location and metadata (e.g. format). 



**Returns**

  * ([::Google::Cloud::Vision::V1p3beta1::OutputConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p3beta1/latest/Google-Cloud-Vision-V1p3beta1-OutputConfig)) — Required. The desired output location and metadata (e.g. format). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
