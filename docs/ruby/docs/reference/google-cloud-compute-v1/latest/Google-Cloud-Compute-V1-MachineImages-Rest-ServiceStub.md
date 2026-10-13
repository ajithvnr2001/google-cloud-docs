---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-MachineImages-Rest-ServiceStub/
title: Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::MachineImages::Rest::ServiceStub (v4.0.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:10:36.889413+00:00
---

# Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::MachineImages::Rest::ServiceStub (v4.0.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-MachineImages-Rest-ServiceStub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::MachineImages::Rest::ServiceStub (v4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.12.0  3.10.0  3.9.1  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.22.0  2.21.1  2.20.0  2.19.1  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.2  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.10.0  1.9.0  1.8.0  1.7.1  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.5.0 

Reference documentation and code samples for the Google Cloud Compute V1 API class Google::Cloud::Compute::V1::MachineImages::Rest::ServiceStub.

REST service stub for the MachineImages service. Service stub contains baseline method implementations including transcoding, making the REST call, and deserialing the response.

## Inherits

  * Object 



## Methods 

### #delete
    
    
    def delete(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Compute::V1::Operation

Baseline implementation for the delete REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Compute::V1::DeleteMachineImageRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-DeleteMachineImageRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Compute::V1::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Compute::V1::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #endpoint
    
    
    def endpoint() -> String

The effective endpoint

**Returns**

  * (String) 



### #get
    
    
    def get(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Compute::V1::MachineImage

Baseline implementation for the get REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Compute::V1::GetMachineImageRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GetMachineImageRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Compute::V1::MachineImage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-MachineImage)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Compute::V1::MachineImage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-MachineImage)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_iam_policy
    
    
    def get_iam_policy(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Compute::V1::Policy

Baseline implementation for the get_iam_policy REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Compute::V1::GetIamPolicyMachineImageRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GetIamPolicyMachineImageRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Compute::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Policy)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Compute::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Policy)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #insert
    
    
    def insert(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Compute::V1::Operation

Baseline implementation for the insert REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Compute::V1::InsertMachineImageRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InsertMachineImageRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Compute::V1::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Compute::V1::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list
    
    
    def list(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Compute::V1::MachineImageList

Baseline implementation for the list REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Compute::V1::ListMachineImagesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ListMachineImagesRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Compute::V1::MachineImageList](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-MachineImageList)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Compute::V1::MachineImageList](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-MachineImageList)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #logger
    
    
    def logger(stub: false) -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #set_iam_policy
    
    
    def set_iam_policy(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Compute::V1::Policy

Baseline implementation for the set_iam_policy REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Compute::V1::SetIamPolicyMachineImageRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-SetIamPolicyMachineImageRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Compute::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Policy)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Compute::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Policy)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #set_labels
    
    
    def set_labels(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Compute::V1::Operation

Baseline implementation for the set_labels REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Compute::V1::SetLabelsMachineImageRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-SetLabelsMachineImageRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Compute::V1::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Compute::V1::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #test_iam_permissions
    
    
    def test_iam_permissions(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Compute::V1::TestPermissionsResponse

Baseline implementation for the test_iam_permissions REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Compute::V1::TestIamPermissionsMachineImageRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-TestIamPermissionsMachineImageRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Compute::V1::TestPermissionsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-TestPermissionsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Compute::V1::TestPermissionsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-TestPermissionsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
