---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video_intelligence-v1p2beta1/latest/Google-Cloud-VideoIntelligence-V1p2beta1-AnnotateVideoResponse/
title: Cloud Video Intelligence V1p2beta1 API - Class Google::Cloud::VideoIntelligence::V1p2beta1::AnnotateVideoResponse (v0.18.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:54:25.617226+00:00
---

# Cloud Video Intelligence V1p2beta1 API - Class Google::Cloud::VideoIntelligence::V1p2beta1::AnnotateVideoResponse (v0.18.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video_intelligence-v1p2beta1/latest/Google-Cloud-VideoIntelligence-V1p2beta1-AnnotateVideoResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Video Intelligence V1p2beta1 API - Class Google::Cloud::VideoIntelligence::V1p2beta1::AnnotateVideoResponse (v0.18.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.18.1 (latest)  0.18.0  0.17.0  0.16.1  0.15.0  0.14.0  0.13.1  0.12.0  0.11.2  0.10.2  0.9.0  0.8.1  0.7.0  0.6.0  0.5.0  0.4.5 

Reference documentation and code samples for the Cloud Video Intelligence V1p2beta1 API class Google::Cloud::VideoIntelligence::V1p2beta1::AnnotateVideoResponse.

Video annotation response. Included in the `response` field of the `Operation` returned by the `GetOperation` call of the `google::longrunning::Operations` service.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #annotation_results
    
    
    def annotation_results() -> ::Array<::Google::Cloud::VideoIntelligence::V1p2beta1::VideoAnnotationResults>

**Returns**

  * (::Array<[::Google::Cloud::VideoIntelligence::V1p2beta1::VideoAnnotationResults](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video_intelligence-v1p2beta1/latest/Google-Cloud-VideoIntelligence-V1p2beta1-VideoAnnotationResults)>) — Annotation results for all videos specified in `AnnotateVideoRequest`. 



### #annotation_results=
    
    
    def annotation_results=(value) -> ::Array<::Google::Cloud::VideoIntelligence::V1p2beta1::VideoAnnotationResults>

**Parameter**

  * **value** (::Array<[::Google::Cloud::VideoIntelligence::V1p2beta1::VideoAnnotationResults](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video_intelligence-v1p2beta1/latest/Google-Cloud-VideoIntelligence-V1p2beta1-VideoAnnotationResults)>) — Annotation results for all videos specified in `AnnotateVideoRequest`. 



**Returns**

  * (::Array<[::Google::Cloud::VideoIntelligence::V1p2beta1::VideoAnnotationResults](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video_intelligence-v1p2beta1/latest/Google-Cloud-VideoIntelligence-V1p2beta1-VideoAnnotationResults)>) — Annotation results for all videos specified in `AnnotateVideoRequest`. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
