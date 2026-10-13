---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p4beta1/latest/Google-Cloud-Vision-V1p4beta1-ImageAnnotator-Rest-ServiceStub/
title: Cloud Vision V1p4beta1 API - Class Google::Cloud::Vision::V1p4beta1::ImageAnnotator::Rest::ServiceStub (v0.16.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:58:11.364935+00:00
---

# Cloud Vision V1p4beta1 API - Class Google::Cloud::Vision::V1p4beta1::ImageAnnotator::Rest::ServiceStub (v0.16.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p4beta1/latest/Google-Cloud-Vision-V1p4beta1-ImageAnnotator-Rest-ServiceStub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Vision V1p4beta1 API - Class Google::Cloud::Vision::V1p4beta1::ImageAnnotator::Rest::ServiceStub (v0.16.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.16.1 (latest)  0.16.0  0.15.1  0.14.1  0.13.0  0.12.1  0.11.1  0.10.0  0.9.0  0.8.1  0.7.2  0.6.0  0.5.1  0.4.0  0.3.0  0.2.0  0.1.2 

Reference documentation and code samples for the Cloud Vision V1p4beta1 API class Google::Cloud::Vision::V1p4beta1::ImageAnnotator::Rest::ServiceStub.

REST service stub for the ImageAnnotator service. Service stub contains baseline method implementations including transcoding, making the REST call, and deserialing the response.

## Inherits

  * Object 



## Methods 

### #async_batch_annotate_files
    
    
    def async_batch_annotate_files(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the async_batch_annotate_files REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Vision::V1p4beta1::AsyncBatchAnnotateFilesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p4beta1/latest/Google-Cloud-Vision-V1p4beta1-AsyncBatchAnnotateFilesRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p4beta1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p4beta1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #async_batch_annotate_images
    
    
    def async_batch_annotate_images(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the async_batch_annotate_images REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Vision::V1p4beta1::AsyncBatchAnnotateImagesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p4beta1/latest/Google-Cloud-Vision-V1p4beta1-AsyncBatchAnnotateImagesRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p4beta1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p4beta1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #batch_annotate_files
    
    
    def batch_annotate_files(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Vision::V1p4beta1::BatchAnnotateFilesResponse

Baseline implementation for the batch_annotate_files REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Vision::V1p4beta1::BatchAnnotateFilesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p4beta1/latest/Google-Cloud-Vision-V1p4beta1-BatchAnnotateFilesRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Vision::V1p4beta1::BatchAnnotateFilesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p4beta1/latest/Google-Cloud-Vision-V1p4beta1-BatchAnnotateFilesResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Vision::V1p4beta1::BatchAnnotateFilesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p4beta1/latest/Google-Cloud-Vision-V1p4beta1-BatchAnnotateFilesResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #batch_annotate_images
    
    
    def batch_annotate_images(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Vision::V1p4beta1::BatchAnnotateImagesResponse

Baseline implementation for the batch_annotate_images REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Vision::V1p4beta1::BatchAnnotateImagesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p4beta1/latest/Google-Cloud-Vision-V1p4beta1-BatchAnnotateImagesRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Vision::V1p4beta1::BatchAnnotateImagesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p4beta1/latest/Google-Cloud-Vision-V1p4beta1-BatchAnnotateImagesResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Vision::V1p4beta1::BatchAnnotateImagesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p4beta1/latest/Google-Cloud-Vision-V1p4beta1-BatchAnnotateImagesResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #endpoint
    
    
    def endpoint() -> String

The effective endpoint

**Returns**

  * (String) 



### #logger
    
    
    def logger(stub: false) -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
