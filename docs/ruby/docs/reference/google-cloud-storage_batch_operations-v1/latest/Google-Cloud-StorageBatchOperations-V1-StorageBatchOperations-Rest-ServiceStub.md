---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_batch_operations-v1/latest/Google-Cloud-StorageBatchOperations-V1-StorageBatchOperations-Rest-ServiceStub/
title: Storage Batch Operations V1 API - Class Google::Cloud::StorageBatchOperations::V1::StorageBatchOperations::Rest::ServiceStub (v1.0.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:48:59.754269+00:00
---

# Storage Batch Operations V1 API - Class Google::Cloud::StorageBatchOperations::V1::StorageBatchOperations::Rest::ServiceStub (v1.0.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_batch_operations-v1/latest/Google-Cloud-StorageBatchOperations-V1-StorageBatchOperations-Rest-ServiceStub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Storage Batch Operations V1 API - Class Google::Cloud::StorageBatchOperations::V1::StorageBatchOperations::Rest::ServiceStub (v1.0.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.1 (latest)  1.0.0  0.10.0  0.9.0  0.8.1  0.7.0  0.6.0  0.5.0  0.4.1  0.3.0  0.2.0  0.1.3 

Reference documentation and code samples for the Storage Batch Operations V1 API class Google::Cloud::StorageBatchOperations::V1::StorageBatchOperations::Rest::ServiceStub.

REST service stub for the StorageBatchOperations service. Service stub contains baseline method implementations including transcoding, making the REST call, and deserialing the response.

## Inherits

  * Object 



## Methods 

### #cancel_job
    
    
    def cancel_job(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::StorageBatchOperations::V1::CancelJobResponse

Baseline implementation for the cancel_job REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::StorageBatchOperations::V1::CancelJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_batch_operations-v1/latest/Google-Cloud-StorageBatchOperations-V1-CancelJobRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::StorageBatchOperations::V1::CancelJobResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_batch_operations-v1/latest/Google-Cloud-StorageBatchOperations-V1-CancelJobResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::StorageBatchOperations::V1::CancelJobResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_batch_operations-v1/latest/Google-Cloud-StorageBatchOperations-V1-CancelJobResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_job
    
    
    def create_job(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the create_job REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::StorageBatchOperations::V1::CreateJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_batch_operations-v1/latest/Google-Cloud-StorageBatchOperations-V1-CreateJobRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_batch_operations-v1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_batch_operations-v1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_job
    
    
    def delete_job(request_pb, options = nil) { |result, operation| ... } -> ::Google::Protobuf::Empty

Baseline implementation for the delete_job REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::StorageBatchOperations::V1::DeleteJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_batch_operations-v1/latest/Google-Cloud-StorageBatchOperations-V1-DeleteJobRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_batch_operations-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_batch_operations-v1/latest/Google-Protobuf-Empty)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #endpoint
    
    
    def endpoint() -> String

The effective endpoint

**Returns**

  * (String) 



### #get_bucket_operation
    
    
    def get_bucket_operation(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::StorageBatchOperations::V1::BucketOperation

Baseline implementation for the get_bucket_operation REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::StorageBatchOperations::V1::GetBucketOperationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_batch_operations-v1/latest/Google-Cloud-StorageBatchOperations-V1-GetBucketOperationRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::StorageBatchOperations::V1::BucketOperation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_batch_operations-v1/latest/Google-Cloud-StorageBatchOperations-V1-BucketOperation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::StorageBatchOperations::V1::BucketOperation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_batch_operations-v1/latest/Google-Cloud-StorageBatchOperations-V1-BucketOperation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_job
    
    
    def get_job(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::StorageBatchOperations::V1::Job

Baseline implementation for the get_job REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::StorageBatchOperations::V1::GetJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_batch_operations-v1/latest/Google-Cloud-StorageBatchOperations-V1-GetJobRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::StorageBatchOperations::V1::Job](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_batch_operations-v1/latest/Google-Cloud-StorageBatchOperations-V1-Job)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::StorageBatchOperations::V1::Job](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_batch_operations-v1/latest/Google-Cloud-StorageBatchOperations-V1-Job)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_bucket_operations
    
    
    def list_bucket_operations(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::StorageBatchOperations::V1::ListBucketOperationsResponse

Baseline implementation for the list_bucket_operations REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::StorageBatchOperations::V1::ListBucketOperationsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_batch_operations-v1/latest/Google-Cloud-StorageBatchOperations-V1-ListBucketOperationsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::StorageBatchOperations::V1::ListBucketOperationsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_batch_operations-v1/latest/Google-Cloud-StorageBatchOperations-V1-ListBucketOperationsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::StorageBatchOperations::V1::ListBucketOperationsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_batch_operations-v1/latest/Google-Cloud-StorageBatchOperations-V1-ListBucketOperationsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_jobs
    
    
    def list_jobs(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::StorageBatchOperations::V1::ListJobsResponse

Baseline implementation for the list_jobs REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::StorageBatchOperations::V1::ListJobsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_batch_operations-v1/latest/Google-Cloud-StorageBatchOperations-V1-ListJobsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::StorageBatchOperations::V1::ListJobsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_batch_operations-v1/latest/Google-Cloud-StorageBatchOperations-V1-ListJobsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::StorageBatchOperations::V1::ListJobsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage_batch_operations-v1/latest/Google-Cloud-StorageBatchOperations-V1-ListJobsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



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

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
