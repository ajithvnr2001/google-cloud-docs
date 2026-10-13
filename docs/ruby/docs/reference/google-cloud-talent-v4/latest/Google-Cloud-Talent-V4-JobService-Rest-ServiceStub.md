---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-JobService-Rest-ServiceStub/
title: Cloud Talent Solution V4 API - Class Google::Cloud::Talent::V4::JobService::Rest::ServiceStub (v1.9.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:18:56.586738+00:00
---

# Cloud Talent Solution V4 API - Class Google::Cloud::Talent::V4::JobService::Rest::ServiceStub (v1.9.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-JobService-Rest-ServiceStub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Talent Solution V4 API - Class Google::Cloud::Talent::V4::JobService::Rest::ServiceStub (v1.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.9.1 (latest)  1.9.0  1.8.1  1.7.0  1.6.1  1.5.0  1.4.0  1.3.1  1.2.0  1.1.0  1.0.1  0.13.0  0.12.2  0.11.0  0.10.1  0.9.1  0.8.1  0.7.0  0.6.4 

Reference documentation and code samples for the Cloud Talent Solution V4 API class Google::Cloud::Talent::V4::JobService::Rest::ServiceStub.

REST service stub for the JobService service. Service stub contains baseline method implementations including transcoding, making the REST call, and deserialing the response.

## Inherits

  * Object 



## Methods 

### #batch_create_jobs
    
    
    def batch_create_jobs(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the batch_create_jobs REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Talent::V4::BatchCreateJobsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-BatchCreateJobsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #batch_delete_jobs
    
    
    def batch_delete_jobs(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the batch_delete_jobs REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Talent::V4::BatchDeleteJobsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-BatchDeleteJobsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #batch_update_jobs
    
    
    def batch_update_jobs(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the batch_update_jobs REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Talent::V4::BatchUpdateJobsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-BatchUpdateJobsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_job
    
    
    def create_job(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Talent::V4::Job

Baseline implementation for the create_job REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Talent::V4::CreateJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-CreateJobRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Talent::V4::Job](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-Job)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Talent::V4::Job](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-Job)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_job
    
    
    def delete_job(request_pb, options = nil) { |result, operation| ... } -> ::Google::Protobuf::Empty

Baseline implementation for the delete_job REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Talent::V4::DeleteJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-DeleteJobRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Protobuf-Empty)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #endpoint
    
    
    def endpoint() -> String

The effective endpoint

**Returns**

  * (String) 



### #get_job
    
    
    def get_job(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Talent::V4::Job

Baseline implementation for the get_job REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Talent::V4::GetJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-GetJobRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Talent::V4::Job](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-Job)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Talent::V4::Job](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-Job)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_jobs
    
    
    def list_jobs(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Talent::V4::ListJobsResponse

Baseline implementation for the list_jobs REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Talent::V4::ListJobsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-ListJobsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Talent::V4::ListJobsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-ListJobsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Talent::V4::ListJobsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-ListJobsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #logger
    
    
    def logger(stub: false) -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #search_jobs
    
    
    def search_jobs(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Talent::V4::SearchJobsResponse

Baseline implementation for the search_jobs REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Talent::V4::SearchJobsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-SearchJobsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Talent::V4::SearchJobsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-SearchJobsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Talent::V4::SearchJobsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-SearchJobsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #search_jobs_for_alert
    
    
    def search_jobs_for_alert(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Talent::V4::SearchJobsResponse

Baseline implementation for the search_jobs_for_alert REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Talent::V4::SearchJobsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-SearchJobsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Talent::V4::SearchJobsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-SearchJobsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Talent::V4::SearchJobsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-SearchJobsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_job
    
    
    def update_job(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Talent::V4::Job

Baseline implementation for the update_job REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Talent::V4::UpdateJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-UpdateJobRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Talent::V4::Job](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-Job)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Talent::V4::Job](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-talent-v4/latest/Google-Cloud-Talent-V4-Job)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
