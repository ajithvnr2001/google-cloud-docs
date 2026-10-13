---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p3beta1/latest/Google-Cloud-Vision-V1p3beta1-SafeSearchAnnotation/
title: Cloud Vision V1p3beta1 API - Class Google::Cloud::Vision::V1p3beta1::SafeSearchAnnotation (v0.20.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:03:31.426107+00:00
---

# Cloud Vision V1p3beta1 API - Class Google::Cloud::Vision::V1p3beta1::SafeSearchAnnotation (v0.20.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p3beta1/latest/Google-Cloud-Vision-V1p3beta1-SafeSearchAnnotation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Vision V1p3beta1 API - Class Google::Cloud::Vision::V1p3beta1::SafeSearchAnnotation (v0.20.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.1 (latest)  0.20.0  0.19.1  0.18.1  0.17.0  0.16.0  0.15.1  0.14.0  0.13.1  0.12.2  0.11.0  0.10.1  0.9.0  0.8.0  0.7.0  0.6.0  0.5.5 

Reference documentation and code samples for the Cloud Vision V1p3beta1 API class Google::Cloud::Vision::V1p3beta1::SafeSearchAnnotation.

Set of features pertaining to the image, computed by computer vision methods over safe-search verticals (for example, adult, spoof, medical, violence).

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #adult
    
    
    def adult() -> ::Google::Cloud::Vision::V1p3beta1::Likelihood

**Returns**

  * ([::Google::Cloud::Vision::V1p3beta1::Likelihood](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p3beta1/latest/Google-Cloud-Vision-V1p3beta1-Likelihood)) — Represents the adult content likelihood for the image. Adult content may contain elements such as nudity, pornographic images or cartoons, or sexual activities. 



### #adult=
    
    
    def adult=(value) -> ::Google::Cloud::Vision::V1p3beta1::Likelihood

**Parameter**

  * **value** ([::Google::Cloud::Vision::V1p3beta1::Likelihood](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p3beta1/latest/Google-Cloud-Vision-V1p3beta1-Likelihood)) — Represents the adult content likelihood for the image. Adult content may contain elements such as nudity, pornographic images or cartoons, or sexual activities. 



**Returns**

  * ([::Google::Cloud::Vision::V1p3beta1::Likelihood](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p3beta1/latest/Google-Cloud-Vision-V1p3beta1-Likelihood)) — Represents the adult content likelihood for the image. Adult content may contain elements such as nudity, pornographic images or cartoons, or sexual activities. 



### #medical
    
    
    def medical() -> ::Google::Cloud::Vision::V1p3beta1::Likelihood

**Returns**

  * ([::Google::Cloud::Vision::V1p3beta1::Likelihood](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p3beta1/latest/Google-Cloud-Vision-V1p3beta1-Likelihood)) — Likelihood that this is a medical image. 



### #medical=
    
    
    def medical=(value) -> ::Google::Cloud::Vision::V1p3beta1::Likelihood

**Parameter**

  * **value** ([::Google::Cloud::Vision::V1p3beta1::Likelihood](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p3beta1/latest/Google-Cloud-Vision-V1p3beta1-Likelihood)) — Likelihood that this is a medical image. 



**Returns**

  * ([::Google::Cloud::Vision::V1p3beta1::Likelihood](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p3beta1/latest/Google-Cloud-Vision-V1p3beta1-Likelihood)) — Likelihood that this is a medical image. 



### #racy
    
    
    def racy() -> ::Google::Cloud::Vision::V1p3beta1::Likelihood

**Returns**

  * ([::Google::Cloud::Vision::V1p3beta1::Likelihood](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p3beta1/latest/Google-Cloud-Vision-V1p3beta1-Likelihood)) — Likelihood that the request image contains racy content. Racy content may include (but is not limited to) skimpy or sheer clothing, strategically covered nudity, lewd or provocative poses, or close-ups of sensitive body areas. 



### #racy=
    
    
    def racy=(value) -> ::Google::Cloud::Vision::V1p3beta1::Likelihood

**Parameter**

  * **value** ([::Google::Cloud::Vision::V1p3beta1::Likelihood](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p3beta1/latest/Google-Cloud-Vision-V1p3beta1-Likelihood)) — Likelihood that the request image contains racy content. Racy content may include (but is not limited to) skimpy or sheer clothing, strategically covered nudity, lewd or provocative poses, or close-ups of sensitive body areas. 



**Returns**

  * ([::Google::Cloud::Vision::V1p3beta1::Likelihood](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p3beta1/latest/Google-Cloud-Vision-V1p3beta1-Likelihood)) — Likelihood that the request image contains racy content. Racy content may include (but is not limited to) skimpy or sheer clothing, strategically covered nudity, lewd or provocative poses, or close-ups of sensitive body areas. 



### #spoof
    
    
    def spoof() -> ::Google::Cloud::Vision::V1p3beta1::Likelihood

**Returns**

  * ([::Google::Cloud::Vision::V1p3beta1::Likelihood](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p3beta1/latest/Google-Cloud-Vision-V1p3beta1-Likelihood)) — Spoof likelihood. The likelihood that an modification was made to the image's canonical version to make it appear funny or offensive. 



### #spoof=
    
    
    def spoof=(value) -> ::Google::Cloud::Vision::V1p3beta1::Likelihood

**Parameter**

  * **value** ([::Google::Cloud::Vision::V1p3beta1::Likelihood](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p3beta1/latest/Google-Cloud-Vision-V1p3beta1-Likelihood)) — Spoof likelihood. The likelihood that an modification was made to the image's canonical version to make it appear funny or offensive. 



**Returns**

  * ([::Google::Cloud::Vision::V1p3beta1::Likelihood](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p3beta1/latest/Google-Cloud-Vision-V1p3beta1-Likelihood)) — Spoof likelihood. The likelihood that an modification was made to the image's canonical version to make it appear funny or offensive. 



### #violence
    
    
    def violence() -> ::Google::Cloud::Vision::V1p3beta1::Likelihood

**Returns**

  * ([::Google::Cloud::Vision::V1p3beta1::Likelihood](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p3beta1/latest/Google-Cloud-Vision-V1p3beta1-Likelihood)) — Likelihood that this image contains violent content. 



### #violence=
    
    
    def violence=(value) -> ::Google::Cloud::Vision::V1p3beta1::Likelihood

**Parameter**

  * **value** ([::Google::Cloud::Vision::V1p3beta1::Likelihood](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p3beta1/latest/Google-Cloud-Vision-V1p3beta1-Likelihood)) — Likelihood that this image contains violent content. 



**Returns**

  * ([::Google::Cloud::Vision::V1p3beta1::Likelihood](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p3beta1/latest/Google-Cloud-Vision-V1p3beta1-Likelihood)) — Likelihood that this image contains violent content. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
